#ifndef PCHILD_H

#define PCHILD_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <signal.h>
#include <fcntl.h>
#include "constants.h"

int lastSig;

void initClone();
void sendPid();
void emptyHandler(int sigNumber);
void clone();

#endif
