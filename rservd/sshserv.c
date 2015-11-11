/*
 * sshserv.c
 *
 * Our remote SSH Server here
 *
 *  Created on: Jan 2, 2015
 *      Author: bkim
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <poll.h>
#include <termios.h>
#include <pty.h>
#include <pthread.h>


#include <libssh/libssh.h>
#include <libssh/server.h>
#include <libssh/callbacks.h>
#include <libssh/sftp.h>

#include "rsftp.h"
#include "zlogs.h"

#define AUTH_USR "thebrownzelfoxofsiberia"
#define AUTH_PWD "thewhitezelfoxofpersia"

#define DSA_KEYFILE "ssh_host_dsa_key"
#define RSA_KEYFILE "ssh_host_rsa_key"


int authenticate(ssh_session sess)
{
	ssh_message message;

	do
	{
		message = ssh_message_get(sess);
		if(!message)
			break;

		switch(ssh_message_type(message))
		{
		case SSH_REQUEST_AUTH:

			switch(ssh_message_subtype(message))
			{
			case SSH_AUTH_METHOD_PASSWORD:

				if(!strcmp(AUTH_USR, ssh_message_auth_user(message)) && !strcmp(AUTH_PWD, ssh_message_auth_password(message)))
				{
					ssh_message_auth_reply_success(message, 0);
					ssh_message_free(message);
					return 1;
				}

				ssh_message_auth_set_methods(message, SSH_AUTH_METHOD_PASSWORD);

				/* not authenticated, send default mesage */

				ssh_message_reply_default(message);
				break;

			case SSH_AUTH_METHOD_NONE:

				ssh_message_auth_set_methods(message, SSH_AUTH_METHOD_PASSWORD);
				ssh_message_reply_default(message);

				return 0;
				break;
			}
			break;

			default:
				ssh_message_auth_set_methods(message, SSH_AUTH_METHOD_PASSWORD);
				ssh_message_reply_default(message);

		}

		ssh_message_free(message);

	} while(1);

	return 0;
}

void * handle_client(void * args)
{
	ssh_session session;
	ssh_channel chan = 0;
	ssh_message message;
	int rc;
	int shell = 0;

	session = (ssh_session)args;
	fprintf(stdout, "new client!\n");

	if(ssh_handle_key_exchange(session))
	{
		fprintf(stderr, "Couldn't handle key exchange %s", ssh_get_error(session));
		return (void *)1;
	}

	ssh_set_auth_methods(session, SSH_AUTH_METHOD_PASSWORD);

	rc = authenticate(session);
	if(!rc)
	{
		fprintf(stdout, "Client authentication failed");
		return (void *)1;
	}

	do
	{
		message = ssh_message_get(session);
        if(message)
        {
        	if(ssh_message_type(message) == SSH_REQUEST_CHANNEL_OPEN && ssh_message_subtype(message) == SSH_CHANNEL_SESSION)
        	{
        		chan = ssh_message_channel_request_open_reply_accept(message);
		        ssh_message_free(message);
		        break;
		    }
        	else
        	{
        		ssh_message_reply_default(message);
		        ssh_message_free(message);
		    }
		}
        else
        {
        	break;
		}

	} while(!chan);

	if(!chan)
	{
		ssh_finalize();
		return (void *)1;
	}

	/* wait for a shell */
	do {
		message=ssh_message_get(session);
		if(message )
		{
			shell = 1;
		    ssh_message_channel_request_reply_success(message);
		}
		else
		{
			break;
		}
	} while(!shell);

	if(!shell)
	{
		return (void *)1;
	}

	printf("it works!\n");
	sftp_session sftp = sftp_server_new(session, chan);
    rc = sftp_server_init(sftp);
    printf("sftp_server_init() returned %d\n", rc);
    sftp_server_version(sftp);
    ssh_event _event = ssh_event_new();
    rc = ssh_event_add_session(_event, session);
    sftp_client_message sftp_c_msg;
    do
    {
    	sftp_c_msg = sftp_get_client_message(sftp);
    	if(sftp_c_msg == NULL)
		{
			continue;
		}

	    handle_sftp_requests(sftp_c_msg, sftp);
	    sftp_client_message_free(sftp_c_msg);

	}while(sftp_c_msg);

	ssh_event_free(_event);
	ssh_free(session);
	pthread_exit(NULL);

	return NULL;
}

int main(int argc, char *argv[])
{
	unsigned int port = 12202;
	int log_func = SSH_LOG_RARE;
	int rc;
	char * banner = "ZelDrive Reverse Proxy";

	ssh_bind sshbind;

	ssh_threads_set_callbacks(ssh_threads_get_pthread());

	ssh_init();
	sshbind = ssh_bind_new();

	ssh_bind_set_blocking(sshbind, 1);

	ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_BINDPORT, &port);
	ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_LOG_VERBOSITY, &log_func);
	ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_DSAKEY, DSA_KEYFILE);
	ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_RSAKEY, RSA_KEYFILE);
	ssh_bind_options_set(sshbind, SSH_BIND_OPTIONS_BANNER, banner);


	if(ssh_bind_listen(sshbind)<0)
	{
		exit(-1);
	}

	while (1)
	{
		ssh_session session = ssh_new();

		rc = ssh_bind_accept(sshbind, session);

		if(rc == SSH_ERROR)
		{
			ssh_free(session);
		}
		else
		{
			pthread_t pthread;
			pthread_create(&pthread, NULL, handle_client, (void *)session);
		}

	}

	ssh_bind_free(sshbind);
	return 0;
}
