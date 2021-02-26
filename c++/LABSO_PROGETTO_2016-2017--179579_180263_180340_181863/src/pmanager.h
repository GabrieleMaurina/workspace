#ifndef PMANAGER_H

#define PMANAGER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <signal.h>
#include <fcntl.h>
#include "constants.h"

typedef struct process_s process;

struct process_s
{
    char* name;
  	int pid;
  	int ppid;
	int dimArr;
	int nClones;
	int active;
	
	process** clones;
};

process* shell;

void test(int argc, char** argv);
void initShell();
void updateAllChildren(process* p);
void killOne(process* p);
void killAll(process* p);
void killShell(process* p);
void printhelp();
int listProcessesAus(process* p);
void listProcesses();
int treeProcessesAus(process* p, int depth);
void treeProcesses();
process* findProcessByName(char* name, process* p);
int readLine (int fd, char *str);
void spawnNew(char* name);
void newProcess(char* name);
void removeAll(char* name);
void closeProcess(char* name);
void info(char* name);
int execute(char** args);
char** splitline(char* line);
char* readcommand();
void loop();


#endif