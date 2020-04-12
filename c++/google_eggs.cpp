#define MAX_N 1000000
#define MAX_K 100

#include <iostream>

using namespace std;

int f(const int n, const int k){
	static int fs[MAX_N-1][MAX_K-1];
	if(k<0||n<0)return -1;
	if(n==0)return 0;
	if(k==0)return -1;
	if(n==1)return 1;
	if(k==1)return n;
	if(fs[n-2][k-2])return fs[n-2][k-2];
	int mn=n;
	int mx;
	for(int i=0; i<n; i++){
		mx=max(f(i,k-1), f(n-i-1,k));
		if(mx<mn)mn=mx;
	}
	fs[n-2][k-2]=++mn;
	return mn;
}

int main(const int argc, const char **argv){
	if(argc==3)cout<<f(stoi(argv[1]), stoi(argv[2]))<<endl;
	return 0;
}
