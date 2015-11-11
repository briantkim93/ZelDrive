/*
 * zlogs.c
 *
 * Zeld logs
 *
 *  Created on: Jan 4, 2015
 *      Author: bkim
 */


#include <stdio.h>
#include <time.h>
#include "zlogs.h"

static FILE * logfile;

void zlog_set_file(const char * file)
{
	logfile = fopen(file, "a");
}

void zlog(const char * info)
{
	time_t curr;
	time(&curr);
	fprintf(logfile, "%s\t%s\n", info, ctime(&curr));
}

void atexit()
{
	fclose(logfile);
}
