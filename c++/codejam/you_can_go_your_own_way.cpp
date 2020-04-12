#include <iostream>

using namespace std;

int t;
unsigned long n;
char c;

int main(int argc, char** argv){
	cin>>t;
	for(int i=1; i<=t; i++){
		cout<<"Case #"<<i<<": ";
		cin>>skipws>>n;
		cin>>c;
		while(1){
			if(c=='E')cout<<'S';
			else if(c=='S')cout<<'E';
			else break;
			cin>>noskipws>>c;
		}
		cout<<endl;
	}
	return 0;
}
