#define l(i,k) for(int i=0; i<k; i++)

#include <iostream>

using namespace std;

int t;

int A;
bool f[3];
char b[501];

int main(int argc, char** argv){
	cin>>t;
	l(tc,t){
		cout<<"Case #"<<tc+1<<": ";
		cin>>A;
		l(i,3)f[i]=0;
		l(i,A){
			cin>>b[0];
			if(b[0]=='R')f[0]=1;
			else if(b[0]=='P')f[1]=1;
			else f[2]=1;
			if(f[0]&&f[1]&&f[2])cout<<"IMPOSSIBLE";
		}
		if(!f[0])cout<<"P";
		if(!f[1])cout<<"S";
		if(!f[0])cout<<"P";
		cout<<endl;
	}
	return 0;
}
