#define MAX 1000000

#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

int gcd(const int a[], const int l){
	if(l<1)return -1;
	int d=a[0];
	for(int i=1; i<l && d>1; i++)d=gcd(d,a[i]);
	return d;
}

int lcm(const int a[], const int l){
	if(l<1)return -1;
	int m=a[0];
	for(int i=1; i<l; i++)m=lcm(m, a[i]);
	return m;
}

bool f(const int k, const int s[], const int l){
	static bool fs[MAX];
	if(k==0)return fs[k]=1;
	for(int i=0; i<l; i++)
		if(k-s[i]>=0 && fs[k-s[i]])return fs[k]=1;
	return fs[k]=0;
}

int chicken_nuggets(int s[], const int l){
	if(gcd(s, l)>1)return -1;
	sort(s, &s[l]);
	int m=lcm(s, l);
	int c=0;
	for(int i=0; i<m && i-c<=s[0]; i++)
		if(!f(i, s, l))c=i;
	return c;
}

int main(const int argc, const char **argv){
	if(argc>1){
		int s[argc-1];
		for(int i=0; i<argc-1; i++)s[i]=stoi(argv[i+1]);
		cout<<chicken_nuggets(s, argc-1)<<endl;
	}
	return 0;
}
