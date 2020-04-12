#ifndef GENERATETEST_H

#define GENERATETEST_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int nProcesses;
int maxClones;
int maxTerminations;// has to be lower than maxProcesses + maxClones
char** processes;

void generateCreationCommands(FILE* file);
void generateCloneCommands(FILE* file);

#endif
