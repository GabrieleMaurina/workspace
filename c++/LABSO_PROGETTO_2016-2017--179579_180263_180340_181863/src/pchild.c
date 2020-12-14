#include "pchild.h"



int main (int argc, char** argv) 
{
	initClone();
	
	while(1)
	{
		clone();
		sleep(1);
	}
	return 0;
}

void initClone()
{
	signal(SIG_SPAWN, emptyHandler);
	signal(SIG_UPDATE, emptyHandler);
	signal(SIGCHLD, SIG_IGN);
	
	sendPid();
}

void sendPid()
{
	lastSig = 0;
	int fd, messageLen, i;
	char message [100];
	
	sprintf(message, "%d",getpid());
	messageLen = strlen(message) + 1;
	
	do 
	{
		fd = open(PIPE_NAME, O_WRONLY);
	} while (fd == -1);
	
	write (fd, message, messageLen);
	close(fd);
}

void clone()
{
	if(lastSig == SIG_SPAWN)
	{
		pid_t pid = fork();
	  	if(pid >= 0)
		{
			if(pid == 0)
			{
				execve("pchild",NULL,NULL);
			}
			else
			{
				lastSig = 0;
			}
	  	}
		else
		{
			printf("Fork unsuccessfull\n");
		}
	}
}

void emptyHandler(int sigNumber)
{
	lastSig = sigNumber;
}
