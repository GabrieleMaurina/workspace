#include <iostream>
#include <cstdint>
#include <set>
#include <unordered_map>
#include <algorithm>

using namespace std;

#define cint uint32_t

int t;
cint n, l;
cint c[100];
set<cint> p;
unordered_map<cint, char> d;

int main(int argc, char** argv){
	cin>>t;
	for(int i=1; i<=t; i++){
		cout<<"Case #"<<i<<": ";
		cin>>n>>l;

		p.clear();
		d.clear();

		for(int i=0; i<l; i++)cin>>c[i];
		cint p1=c[0]%2?3:2;
		while(c[0]%p1)p1+=2;
		cint p2=c[0]/p1;

		int j=1;
		while(c[0]==c[j])j++;
		if((j%2 && c[j]%p2)||(j%2==0 && c[j]%p1))p1=p2;
		p.insert(p1);
		p2=p1;

		for(int i=0; i<l; i++){
			c[i]/=p2;
			p2=c[i];
			p.insert(p2);
		}

		j=0;
		for(auto pr : p)d.insert({pr, (char)65+j++});

		cout<<d[p1];
		for(int i=0; i<l; i++)cout<<d[c[i]];
		cout<<endl;
	}
	return 0;
}
