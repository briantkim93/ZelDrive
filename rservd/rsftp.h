/*
 * rsftp.h
 *
 *  Created on: Apr 17, 2015
 *      Author: bkim
 */

#ifndef RSFTP_H_
#define RSFTP_H_

#include <libssh/libssh.h>
#include <libssh/sftp.h>

void handle_sftp_requests(sftp_client_message, sftp_session);

#endif /* RSFTP_H_ */
