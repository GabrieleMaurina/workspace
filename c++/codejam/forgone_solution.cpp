#include <iostream>

using namespace std;

int t;
char n[100];
char a[100];
char b[100];

int main(int argc, char** argv){
	cin>>t;
	for(int i=1; i<=t; i++){
		cout<<"Case #"<<i<<": ";
		cin>>n;
		for(int i=0; n[i]; i++){
			if(n[i]=='4')a[i]=b[i]='2';
			else{
				a[i]=n[i];
				b[i]='0';
			}
			cout<<a[i];
		}
		cout<<' ';
		bool p=0;
		for(int i=0; n[i]; i++)
			if(p)cout<<b[i];
			else if(b[i]!='0'){
				p=1;
				cout<<b[i];
			}
		cout<<endl;
	}
	return 0;
}
