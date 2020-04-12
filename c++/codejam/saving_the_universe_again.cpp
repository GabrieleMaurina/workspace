#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdint>
#include <cmath>

using namespace std;

#define in cin
#define out cout
//ifstream in("input.in");
//ofstream out("output.out");

uint32_t t, d, s, y, cc, dd;
char p[30];
uint8_t c[30];

int dmg(){
	dd=0;
	int ddd=1;
	cc=0;
	for(int i=0; i<s; i++){
		if(p[i]=='C'){
			ddd*=2;
			c[cc++]=i;
		}
		else dd+=ddd;
	}
	return dd;
}

void hack(){
	for(int j=cc-1; j>=0; j--){
		while(dd>d && c[j]<s+j-cc){
			c[j]++;
			dd-=pow(2, j);
			y++;
		}
	}
}

int main(int argc, char** argv){
	in>>t;
	for(int i=1; i<=t; i++){
		cout<<"Case #"<<i<<": ";
		y=0;
		in>>d>>p;
		s=strlen(p);
		dmg();
		hack();
		if(dd>d) out<<"IMPOSSIBLE"<<endl;
		else out<<y<<endl;
	}
	return 0;
}
