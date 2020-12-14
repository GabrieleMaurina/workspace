#include "pmanager.h"



void killOne(process* p)
{
	p -> active = 0;
	kill(p -> pid, SIGTERM);
}

void killAll(process* p)
{
	int i;
	for(i = 0; i < p -> nClones; i++)
	{
		killAll(p -> clones[i]);
	}
	
	killOne(p);
}

void killShell(process* p)
{
	int i;
	for(i = 0; i < p -> nClones; i++)
	{
		killAll(p -> clones[i]);
	}
}

void printhelp()
{
	printf("Commands:\n");
    printf("\t- phelp : lists available commands\n");
    printf("\t- plist : lists all processes\n");
    printf("\t- pnew <name> : creates new process with name <name>\n");
    printf("\t- pinfo <name> : gives info about process with name <name>\n");
    printf("\t- pclose <name> : terminates process with name <name>\n");
    printf("\t- quit : closes every process\n");
    printf("\t- pspawn <nome> : clones process with name <name> creating a new one with name <name_i> with increasing i\n");
    printf("\t- prmall <nome> : terminates process with name <name> and each of its clones and subclones\n");
    printf("\t- ptree : shows full hierarchy of generated processes\n\n");
}

int listProcessesAus(process* p)
{
	int i;
	for(i = 0; i < p -> nClones; i++)
	{
		process* c = p -> clones[i];
		printf("Nome: %s\n", c -> name);
		printf("Pid: %i\n", c -> pid);
		printf("PPid: %i\n", c -> ppid);
		if(c -> active == 1)
		{
			printf("Status: Running\n");
		}
		else
		{
			printf("Status: Stopped\n");
		}
		printf("\n");
		listProcessesAus(c);
	}
	return p -> nClones;
}

void updateAllChildren(process* p)
{
	int i;
	int test;
	for(i = 0; i < p -> nClones; i++)
	{
		test = kill(p -> clones[i] -> pid, SIG_UPDATE);
		p -> clones[i] -> active = (p -> clones[i] -> active && !(-test));
		updateAllChildren(p -> clones[i]);
	}
}

void listProcesses()
{
	printf("List of processes:\n\n");
	if(!listProcessesAus(shell))
	{
		printf("No processes to show\n\n");
	}
}


int treeProcessesAus(process* p, int depth)
{
	int i;
	int j;
	
	for(i = 0; i < p -> nClones; i++)
	{
		for(j = 0; j < depth; j++)
		{
			printf("\t");	
		}
		
		process* c = p -> clones[i];
		printf("%s (%s)\n", c -> name, (c -> active) ? "running" : "stopped");
		treeProcessesAus(c, depth + 1);
	}
	
	return p -> nClones;
}

void treeProcesses()
{
	printf("Hierarchy of processes:\n\n");
	
	if(!treeProcessesAus(shell, 0))
	{
		printf("No processes to show\n");
	}
	
	printf("\n");
}

process* findProcessByName(char* name, process* p)
{
	int i;
	for(i = 0; i < p -> nClones; i++)
	{
		process* toRtn = findProcessByName(name, p -> clones[i]);
		
		if(toRtn != NULL)
		{
			return toRtn;
		}
	}
	
	if(strcmp(p -> name,name) == 0)
	{
		return p;
	}
	
	return NULL;
}

int readLine (int fd, char *str)
{
	int n;
	do
	{
		n = read (fd, str, 1);
	} while (n > 0 && *str++ != '\0');
	
	return (n > 0);
}

void spawnNew(char* name)
{
	if(name != NULL)
	{
		process* p = findProcessByName(name, shell);
		if(p != NULL)
		{
			if(p -> active != 0)
			{
				int fd;
				char str[100];
				
				unlink(PIPE_NAME);
				mknod (PIPE_NAME, S_IFIFO, 0);
				chmod (PIPE_NAME, S_IRWXU | S_IRWXG | S_IRWXO);
				
				kill(p -> pid, SIG_SPAWN);
				
				fd = open(PIPE_NAME, O_RDONLY);
				
				strcpy(str,"");
				while(!strlen(str))
				{
					readLine(fd, str);
				}
				
				int pid = atoi(str);
				
				close (fd);
				unlink(PIPE_NAME);
				
				process* c = malloc(sizeof(process));
				
				char buffer1[100];
				char buffer2[100];
				sprintf(buffer1,"_%d",p -> nClones + 1); 
				strcpy(buffer2,p -> name);
				strcat(buffer2,buffer1);
				
				c -> name = strdup(buffer2);
	  			c -> pid = pid;
	  			c -> ppid = p -> pid;
				c -> dimArr = 2;
				c -> nClones = 0;
				c -> active = 1;
				c -> clones = malloc(sizeof(process*) * c -> dimArr);
	  			p -> clones[p -> nClones] = c;
				p -> nClones++;
				
				printf("Process cloned with name \"%s\"\n",c -> name);
			}
			else
			{
				printf("Selected process has already been terminated\n");
			}
		}
		else
		{
			printf("Process not found\n");
		}
	}
	else
	{
		printf("Invalid name\n");
	}
	
	printf("\n");
}

void newProcess(char* name)
{
	if(name != NULL)
	{
		if(findProcessByName(name, shell) == NULL)
		{
		  	pid_t testPid = fork();
		  	if(testPid >= 0)
			{
				if(testPid == 0)
				{
					execve("pchild",NULL,NULL);
				}
				else
				{
					int fd;
					char str[100];
					
					unlink(PIPE_NAME);
					mknod (PIPE_NAME, S_IFIFO, 0);
					chmod (PIPE_NAME, S_IRWXU | S_IRWXG | S_IRWXO);
					fd = open(PIPE_NAME, O_RDONLY);
					
					strcpy(str,"");
					while(!strlen(str))
					{
						readLine(fd, str);
					}
					
					close (fd);
					unlink(PIPE_NAME);
					
		  			if(shell -> nClones >= shell -> dimArr)
					{
		  				shell -> dimArr = shell -> dimArr * 2;
		  				shell -> clones = realloc(shell -> clones, sizeof(process*) * shell -> dimArr);
		  			}
		  			
		  			process* p = malloc(sizeof(process));
					p -> name = strdup(name);
		  			p -> pid = testPid;
		  			p -> ppid = getpid();
					p -> dimArr = 2;
					p -> nClones = 0;
					p -> active = 1;
					p -> clones = malloc(sizeof(process*) * p -> dimArr);
		  			shell -> clones[shell -> nClones] = p;
					shell -> nClones++;
					
					printf("Process created with name \"%s\"\n",name);
		  		}
		  	}
			else
			{
		  		printf("Fork unsuccessfull\n");
		  	}
		}
		else
		{
			printf("A process with name \"%s\" already exists\n",name);
		}
	}
	else
	{
		printf("Invalid name\n");
	}
	
	printf("\n");
}

void removeAll(char* name)
{
	if(name != NULL)
	{
		process* p = findProcessByName(name, shell);
		if(p != NULL)
		{
			killAll(p);
			printf("Process terminated\n");
		}
		else
		{
			printf("Process not found\n");
		}
	}
	else
	{
		printf("Invalid name\n");
	}
	printf("\n");
}

void closeProcess(char* name)
{
	if(name != NULL)
	{
		process* p = findProcessByName(name, shell);
		if(p != NULL)
		{
			if(p -> active != 0)
			{
				killOne(p);
				printf("Process terminated\n");
			}
			else
			{
				printf("Selected process has already been terminated");
			}
		}
		else
		{
			printf("Process not found\n");
		}
	}
	else
	{
		printf("Invalid name\n");
	}
	printf("\n");
}

void info(char* name)
{
	if(name != NULL)
	{
		process* p = findProcessByName(name, shell);
		if(p != NULL)
		{
			printf("\n\tName: \"%s\"\n\tPID: %d\n\tPPID: %d\n\n", p -> name, p -> pid, p -> ppid);
		}
		else
		{
			printf("Process not found\n");
		}
	}
	else
	{
		printf("Invalid name\n");
	}
	printf("\n");
}

int execute(char** args)
{
    if (args[0] == NULL)
	{
    	printf("Invalid command (\"phelp\" for list of commands)\n\n");
    }
    else if(strcmp(args[0], "quit") == 0)
	{
		killShell(shell);
        return 0;
    }
    else if(strcmp(args[0], "phelp") == 0)
	{
        printhelp();
    }
	else if(strcmp(args[0], "plist") == 0)
	{
		listProcesses();
	}
	else if(strcmp(args[0], "ptree") == 0)
	{
		treeProcesses();
	}
	else if(strcmp(args[0], "pnew") == 0)
	{
		newProcess(args[1]);
	}
	else if(strcmp(args[0], "pclose") == 0)
	{
	  	closeProcess(args[1]);
	}
	else if(strcmp(args[0], "pinfo")== 0)
	{
		info(args[1]);
	}
	else if(strcmp(args[0], "prmall")== 0)
	{
		removeAll(args[1]);
	}
	else if(strcmp(args[0], "pspawn")== 0)
	{
		spawnNew(args[1]);
	}
	else
	{
		printf("Invalid command (\"phelp\" for list of commands)\n\n");
	}
    return 1;
}

char** splitline(char* line)
{
    int bufsize = 10;
    int index = 0;
    char **tokens = malloc(bufsize * sizeof(char*));
    char *temp;

    temp = strtok(line, " \n");
    
    while (temp != NULL)
	{
    	tokens[index] = temp;
     	index++;
        temp = strtok(NULL, " \n");
    }
    
	tokens[index] = NULL;
	int i = 0;
	while(i < index)
	{
	  	i++;
	}
	
	return tokens;
}

char* readcommand()
{
    char* buffer = NULL;
    ssize_t buffsize = 0;
    
    printf(">");
    getline(&buffer, &buffsize, stdin);
    return buffer;
}

void loop()
{
    char *line;
    char **args;
    int status = 1;
    
    while(status)
	{
		line = readcommand();
		args = splitline(line);
		updateAllChildren(shell);
		status = execute(args);
		free(line);
		free(args);
    }
}

void initShell()
{
	signal(SIGCHLD, SIG_IGN);
	shell = malloc(sizeof(process));
	shell -> dimArr = 2;
	shell -> clones = malloc(sizeof(process*) * shell -> dimArr);
	shell -> name = "";
	shell -> pid = getpid();
	shell -> ppid = getppid();
	shell -> nClones = 0;
	shell -> active = 1;
}

void test(int argc, char** argv)
{
	if(argc > 1)
	{
		char** args;
		int status = 1;
		FILE* f;
		char buffer[100];
		char bufAus[10];
		
		f = fopen(argv[1], "r");
		if(f != NULL)
		{
			while(fgets(buffer, sizeof buffer, f) != NULL)
			{
				printf("%s\n", buffer);
				args = splitline(buffer);
				updateAllChildren(shell);
				status = execute(args);
				free(args);
				if(status == 0)
				{
					exit(0);
				}
			}
			fclose(f);
		}
		else
		{
			printf("File not found\n");
		}
	}
}

int main(int argc, char** argv)
{
	initShell();
	test(argc,argv);
	loop();
    
    return 0;
}
