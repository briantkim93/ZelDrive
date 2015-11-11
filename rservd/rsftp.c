/*
 * rsftp.c
 *
 *  Created on: Apr 11, 2015
 *      Author: bkim
 */


#include <sys/dirent.h>
#include <sys/stat.h>
#include <sys/statvfs.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <ftw.h>
#include <errno.h>

#include <libssh/libssh.h>
#include <libssh/sftp.h>

#define START_DIR "zfolders/"

/*
 * I don't quite understand the file flags from the sftp_message
 * So I defined mine and then mapped them to those recieved
 */

typedef enum
{
	ZFS_APPEND = 0x0,
	ZFS_READ = 0x1,
	ZFS_WRITE = 0x3,
	ZFS_CREATE = 0x11,
	ZFS_TRUNC = 0x21
}ZFS_FILE_OP;

typedef struct
{
	int fd;
	int how;
	long dirpos;
}ZFS_FILE_DES_STRUCT, * ZFS_FILE_DES;

typedef struct
{
	long data;
}ZFS_S_MSG;

unsigned long num_root_children;

static const char * absolute_path(const char * path)
{
	char * abs_path = (char *)malloc(1 + strlen(path) + strlen(START_DIR));

	strcpy(abs_path, START_DIR);
	strcat(abs_path, path);

	return abs_path;
}

void ensure_start_dir()
{
	DIR * dp = opendir(START_DIR);
	if(dp == NULL)
	{
		mkdir(START_DIR, S_IRWXU | S_IRWXO | S_IRWXG);
	}

	closedir(dp);
}


static sftp_attributes get_stat(const char * path, int stat_type, int fd)
{
	sftp_attributes attr;
	const char * fullpath;
	struct stat buf;

	fullpath = absolute_path(path);

	attr = (sftp_attributes)malloc(sizeof(struct sftp_attributes_struct));

	switch(stat_type)
	{
	case 0x0: //lstat
		lstat(fullpath, &buf);
		break;
	case 0x1: //stat
		stat(fullpath, &buf);
		break;
	case 0x2: //fstat
		fstat(fd, &buf);
	}

	attr->atime = (uint32_t)buf.st_atim.tv_sec;
	attr->atime64 = buf.st_atim.tv_sec;
	attr->atime_nseconds = buf.st_atim.tv_nsec;
	attr->createtime = buf.st_ctim.tv_sec;
	attr->createtime_nseconds = buf.st_ctim.tv_nsec;
	attr->flags = buf.st_mode;
	attr->permissions = buf.st_mode;
	attr->gid = buf.st_gid;
	attr->mtime = (uint32_t)buf.st_mtim.tv_sec;
	attr->mtime64 = buf.st_mtim.tv_sec;
	attr->mtime_nseconds = buf.st_mtim.tv_nsec;
	attr->uid = buf.st_uid;
	attr->size = buf.st_size;


	free((void *)fullpath);

	return attr;
}



sftp_file zfs_open(const char * path, int flags, mode_t mode, sftp_session sftp)
{
	const char * fullpath = absolute_path(path);

	printf("Asked to open file %s\n", path);

	sftp_file file = NULL;
	ZFS_FILE_DES zfs_des = NULL;
	int fd, open_flags = 0;
	struct stat buf;

	switch(flags)
	{
	case ZFS_READ:
		open_flags |= O_RDONLY;
		open_flags |= O_APPEND;
		break;
	case ZFS_CREATE:
		open_flags |= O_CREAT;
		break;
	case ZFS_WRITE:
		open_flags |= O_WRONLY;
		open_flags |= O_APPEND;
		break;
	case ZFS_TRUNC:
		open_flags |= O_TRUNC;
		break;
	default:
		open_flags |= O_WRONLY;
		open_flags |= O_APPEND;

	}

	zfs_des = (ZFS_FILE_DES)malloc(sizeof(ZFS_FILE_DES_STRUCT));
	if(zfs_des == NULL)
	{
		printf("ZFS_FILE_DESCRIPTOR failed to be allocated\n");
		return NULL;
	}

	fd = open(fullpath, open_flags, mode);


	zfs_des->fd = fd;
	zfs_des->how = open_flags;
	zfs_des->dirpos = -1;

	if(fd == -1)
	{
		printf("Error : %s\n", strerror(errno));
	}


	file = (sftp_file)malloc(sizeof(struct sftp_file_struct));

	if(file == NULL)
	{
		printf("SFTP_FILE failed to allocate\n");
		return NULL;
	}


	ssh_string hnd = ssh_string_new(sizeof(ZFS_FILE_DES_STRUCT));
	ssh_string_fill(hnd, zfs_des, sizeof(ZFS_FILE_DES_STRUCT));

	if(hnd == NULL)
	{
		printf("HND failed to allocate\n");
		return NULL;
	}

	lstat(fullpath, &buf);

	file->handle = hnd;
	file->name = strdup(fullpath);
	file->eof = buf.st_size;
	file->offset = 0;
	file->sftp = sftp;

	free((void *)fullpath);
	free(zfs_des);

	return file;
}

size_t zfs_fread(sftp_file file, void * buf, size_t count, off_t offset)
{
	int bytes_r;
	ZFS_FILE_DES zfs_des;

	zfs_des = (ZFS_FILE_DES)ssh_string_data(file->handle);

	printf("About to start reading file - %s for %d bytes ", file->name, count);
	printf("File offset is - %llu\n", offset);

	int r = lseek(zfs_des->fd, offset, SEEK_SET);
	if(r == -1)
	{
		printf("LSEEK error : %s", strerror(errno));
	}

	bytes_r = read(zfs_des->fd, buf, count);

	printf("Just read bytes %d\n", bytes_r);

	return bytes_r;
}

size_t zfs_fwrite(sftp_file file, const void * buf, size_t count, off_t offset)
{
	size_t bytes_w = 2;
	ZFS_FILE_DES zfs_des;
	printf("Asked to write file\n");

	zfs_des = (ZFS_FILE_DES)ssh_string_data(file->handle);

	if(zfs_des == NULL)
	{
		printf("zfs des is null\n");
		return -1;
	}

	printf("Handle requested %d\n", zfs_des->fd);

	if(zfs_des->fd == -1)
	{
		return -1;
	}


	lseek(zfs_des->fd, offset, SEEK_SET);


	bytes_w = write(zfs_des->fd, buf, count);
	if(bytes_w == -1)
	{
		printf("Error occured in write : %s\n", strerror(errno));
	}

	printf("%llu - offset, bytes written %d\n", offset, bytes_w);

	return bytes_w;
}



int zfs_mkdir(const char * path, int mode)
{
	const char * fullpath = absolute_path(path);
	int rc;
	rc = mkdir(fullpath, mode);

	printf("creating dir %s with result %d\n", fullpath, rc);

	free((void *)fullpath);

	return rc;
}


sftp_dir zfs_opendir(const char * path, sftp_session sftp)
{
	const char * fullpath = absolute_path(path);
	DIR * dp;
	ZFS_FILE_DES zfs_des;
	ssh_string hnd;
	sftp_dir dir = (sftp_dir)malloc(sizeof(struct sftp_dir_struct));

	dp = opendir(fullpath);
	zfs_des = (ZFS_FILE_DES)malloc(sizeof(ZFS_FILE_DES_STRUCT));

	memset(zfs_des, 0, sizeof(ZFS_FILE_DES_STRUCT));

	hnd = ssh_string_new(sizeof(ZFS_FILE_DES_STRUCT));

	zfs_des->dirpos = telldir(dp);
	zfs_des->how = -1;

	ssh_string_fill(hnd, zfs_des, sizeof(ZFS_FILE_DES_STRUCT));

	dir->handle = hnd;
	dir->name = strdup(fullpath);
	dir->sftp = sftp;

	int c = 0;

	while(readdir(dp) != NULL)
	{
		c++;
	}

	dir->eof = c;

	free((void *)fullpath);
	free(zfs_des);

	closedir(dp);

	return dir;
}

sftp_attributes zfs_readdir(sftp_dir dir)
{
	sftp_attributes attr;
	ZFS_FILE_DES zfs_des;
	struct dirent * ent;
	struct stat buf;
	char fbuf[1024];
	const char * fbuf_pt;

	DIR * dp = opendir(dir->name);

	zfs_des = (ZFS_FILE_DES)ssh_string_data(dir->handle);

	seekdir(dp, zfs_des->dirpos);

	ent = readdir(dp);

	zfs_des->dirpos = telldir(dp);

	if(ent == NULL)
	{
		printf("ent is null\n");
		return NULL;
	}

	printf("ent is not null\n");

	strcat(fbuf, dir->name);
	strcat(fbuf, "/");
	strcat(fbuf, ent->d_name);

	lstat(ent->d_name, &buf);
	fbuf_pt = fbuf;

	attr = get_stat(fbuf_pt, 0x0, 0); //lstat

	attr->name = ent->d_name;
	attr->type = ent->d_type;

	closedir(dp);

	return attr;
}


sftp_attributes zfs_stat(const char *path)
{
	sftp_attributes attr;

	attr = get_stat(path, 0x1, 0);

	return attr;
}

sftp_attributes zfs_lstat(const char *path)
{
	sftp_attributes attr;

	attr = get_stat(path, 0x0, 0);

	return attr;
}

sftp_attributes zfs_fstat(sftp_file file)
{
	sftp_attributes attr;
	ZFS_FILE_DES des;

	des = (ZFS_FILE_DES)sftp_handle(file->sftp, file->handle);

	attr = get_stat("", 0x2, des->fd);

	return attr;
}

sftp_statvfs_t zfs_statvfs()
{
	sftp_statvfs_t stat_vfs = (sftp_statvfs_t)malloc(sizeof(struct sftp_statvfs_struct));
	struct statvfs vfs;

	statvfs("/", &vfs);

	stat_vfs->f_bavail = vfs.f_bavail;
	stat_vfs->f_bfree = vfs.f_bfree;
	stat_vfs->f_blocks = vfs.f_blocks;
	stat_vfs->f_bsize = vfs.f_bsize;
	stat_vfs->f_favail = vfs.f_favail;
	stat_vfs->f_ffree = vfs.f_ffree;
	stat_vfs->f_flag = vfs.f_flag;
	stat_vfs->f_frsize = vfs.f_frsize;
	stat_vfs->f_fsid = vfs.f_fsid;
	stat_vfs->f_namemax = vfs.f_namemax;

	/* stat_vfs->f_files will be set by the client */

	return stat_vfs;
}


int zfs_unlink(const char * path)
{
	const char * fullpath = absolute_path(path);
	int rc;
	rc = unlink(fullpath);

	free((void *)fullpath);

	return rc;
}

int zfs_rmdir(const char * path)
{
	const char * fullpath = absolute_path(path);
	int rc;
	rc = rmdir(fullpath);

	free((void *)fullpath);

	return rc;
}

int zfs_close(sftp_file file)
{
	ZFS_FILE_DES des;
	int rs;

	des = ssh_string_data(file->handle);

	rs = close(des->fd);

	if(rs == 0)
	{
		printf("File Successfully closed\n");
	}
	else
	{
		printf("Error closing file\n");
	}

	ssh_string_burn(file->handle);
	ssh_string_free(file->handle);
	free(file->name);

	free(file);

	return rs;
}

int zfs_closedir(sftp_dir dir)
{
	ssh_string_burn(dir->handle);
	ssh_string_free(dir->handle);

	free(dir);

	return 0;
}

int zfs_rename(const char * oldpath, const char * newpath)
{
	const char * _oldpath = absolute_path(oldpath);
	const char * _newpath = absolute_path(newpath);
	int rc = rename(_oldpath, _newpath);

	free((void *)_oldpath);
	free((void *)_newpath);

	return rc;
}

int count_root_children(const char *path, const struct stat *st, int typeflag, struct FTW *ftwbuf)
{
	num_root_children++;
	return 0;
}

void handle_sftp_requests(sftp_client_message msg, sftp_session sftp)
{
	uint8_t req = sftp_client_message_get_type(msg);
	sftp_file r_open_file;
	sftp_dir r_open_dir;
	sftp_attributes sftp_attr;
	ZFS_S_MSG zfs_info;
	ZFS_FILE_DES zfs_des;

	ssh_string hnd;

	const char * o_path, * n_path;
	void * buf;

	int status;

	ensure_start_dir();

	switch(req)
	{
	case SSH_FXP_OPEN:
		r_open_file = zfs_open((const char *)msg->filename, msg->flags, msg->attr->permissions, sftp);
		hnd = sftp_handle_alloc(sftp, r_open_file);
		sftp_reply_handle(msg, hnd);
		break;
	case SSH_FXP_OPENDIR:
		//let's see if the client is asking for the total number of children of the directory

		ssh_channel_read(msg->sftp->channel, &zfs_info, sizeof(ZFS_S_MSG), 0);
		if(zfs_info.data > 0)
		{
			num_root_children = 0;
			nftw(msg->filename, count_root_children, 64, FTW_DEPTH | FTW_PHYS);
			zfs_info.data = num_root_children;

			ssh_channel_write(msg->sftp->channel, &zfs_info, sizeof(ZFS_S_MSG));
		}

		r_open_dir = zfs_opendir((const char *)msg->filename, sftp);
		hnd = sftp_handle_alloc(sftp, r_open_dir);
		sftp_reply_handle(msg, hnd);

		break;
	case SSH_FXP_MKDIR:
		sftp_attr = msg->attr;
		status = zfs_mkdir((const char *)msg->filename, sftp_attr->permissions);
		sftp_reply_status(msg, status, "mkdir status result");
		break;
	case SSH_FXP_REMOVE:
		status = zfs_unlink((const char *)msg->filename);
		sftp_reply_status(msg, status, "unlink status result");
		break;
	case SSH_FXP_RMDIR:
		status = zfs_rmdir((const char *)msg->filename);
		sftp_reply_status(msg, status, "rmdir status result");
		break;
	case SSH_FXP_READ:
		hnd = msg->handle;
		r_open_file = (sftp_file)sftp_handle(sftp, hnd);
		printf("RSERVD asked to read file - %s length -%d\n", r_open_file->name, msg->len);
		buf = malloc(msg->len);
		uint32_t b_read = zfs_fread(r_open_file, buf, msg->len, msg->offset);
		sftp_reply_data(msg, buf, b_read);
		free(buf);
		break;
	case SSH_FXP_WRITE:
		hnd = msg->handle;
		r_open_file = (sftp_file)sftp_handle(sftp, hnd);
		uint32_t b_written = zfs_fwrite(r_open_file, ssh_string_data(msg->data), ssh_string_len(msg->data), msg->offset);
		sftp_reply_status(msg, b_written, "");
		zfs_info.data = b_written;

		ssh_channel_write(r_open_file->sftp->channel, &zfs_info, sizeof(ZFS_S_MSG));

		break;

	case SSH_FXP_READDIR:
		hnd = msg->handle;
		r_open_dir = (sftp_dir)sftp_handle(sftp, hnd);
		sftp_attr = zfs_readdir(r_open_dir);

		if(sftp_attr != NULL)
			sftp_reply_name(msg, (const char *)sftp_attr->name, sftp_attr);
		else
			sftp_reply_name(msg, "", NULL);

		break;
	case SSH_FXP_CLOSE:
		hnd = msg->handle;
		buf = sftp_handle(sftp, hnd);
		status = 0;

		r_open_file = (sftp_file)buf;
		zfs_des = (ZFS_FILE_DES)ssh_string_data(r_open_file->handle);

		if(zfs_des->dirpos == -1 && zfs_des->how > 0)
		{
			printf("closing file\n");
			status = zfs_close(r_open_file);
		}
		else
		{
			printf("closing dir\n");
			r_open_dir = (sftp_dir)buf;
			status = zfs_closedir(r_open_dir);
		}

		sftp_handle_remove(msg->sftp, r_open_file);
		sftp_reply_status(msg, status, "file close status");
		break;
	case SSH_FXP_STAT:
		sftp_attr = zfs_stat((const char *)msg->filename);
		sftp_reply_attr(msg, sftp_attr);
		ssh_channel_write(msg->sftp->channel, sftp_attr, sizeof(struct sftp_attributes_struct));
		break;
	case SSH_FXP_LSTAT:
		sftp_attr = zfs_lstat((const char *)msg->filename);
		sftp_reply_attr(msg, sftp_attr);
		ssh_channel_write(msg->sftp->channel, sftp_attr, sizeof(struct sftp_attributes_struct));
		break;
	case SSH_FXP_FSTAT:
		hnd = msg->handle;
		r_open_file = (sftp_file)sftp_handle(sftp, hnd);
		sftp_attr = zfs_fstat(r_open_file);
		sftp_reply_attr(msg, sftp_attr);
		ssh_channel_write(msg->sftp->channel, sftp_attr, sizeof(struct sftp_attributes_struct));
		break;
	case SSH_FXP_RENAME:
		o_path = msg->filename;
		n_path = ssh_string_to_char(msg->data);
		status = zfs_rename(o_path, n_path);
		sftp_reply_status(msg, status, "file rename operation");
		break;
	default:
		sftp_reply_status(msg, -50, "unsupported sftp operation");

	}


}








