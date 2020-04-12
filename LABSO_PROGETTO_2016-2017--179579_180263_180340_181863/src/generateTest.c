#include "generateTest.h"



int main(int argc, char** argv)
{
	srand(time(0));
	
	FILE* f;
	f = fopen("./assets/test", "w");
	
	nProcesses = 100;
	maxClones = rand() % (nProcesses + 200);
	processes = malloc(sizeof(char*) * nProcesses);
	
	generateCreationCommands(f);
	generateCloneCommands(f);
	
	close(f);
	return 0;
}

void generateCreationCommands(FILE* file)
{
	int i;
	int j;
	int nameCounter = 0;
	char* buf1;
	char* buf2;
	
	for(i = 0; i < nProcesses; i++)
	{
		buf1 = malloc(sizeof(char) * 30);
		buf2 = malloc(sizeof(char) * 20);
		strcpy(buf1, "pnew ");
		if(i % 24 == 0 && i > 0)
		{
			nameCounter++;
		}
		for(j = 0; j <= nameCounter; j++)
		{
			buf2[j] = 'a' + (i % 24);
		}
		printf("%s\n", buf2);
		processes[i] = strdup(buf2);
		strcat(buf1, buf2);
		memset(buf2,'\0',20);
		buf2[0] = '\n';
		strcat(buf1, buf2);
		fprintf(file, buf1);
		free(buf1);
		free(buf2);
	}
}

void generateCloneCommands(FILE* file)
{
	int i;
	char* buf1;
	char* buf2;
	int random;
	for(i = 0; i < maxClones; i++)
	{
		buf1 = malloc(sizeof(char) * 30);
		buf2 = malloc(sizeof(char) * 20);
		strcpy(buf1, "pspawn ");
		random = rand() % nProcesses;
		printf("%i\n",random);
		buf2 = strdup(processes[random]);
		strcat(buf1, buf2);
		memset(buf2,'\0',20);
		buf2[0] = '\n';
		strcat(buf1, buf2);
		fprintf(file, buf1);
		free(buf1);
		free(buf2);
	}
}
