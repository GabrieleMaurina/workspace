#define l(i,k) for(int i=0; i<k; i++)

#include <iostream>
#include <algorithm>

using namespace std;

int t;
int n, b, f;
int g;
int gs[1024];
int gs1[1024];
int r;

void compute(int s){
	if(s==1) return;
	l(i,n)
		if((i/(s/2))%2)cout<<'1';
		else cout<<'0';
	cout<<endl;
	char c;
	l(i,g){
		gs1[i*2]=gs1[i*2+1]=0;
		l(j,gs[i]){
			cin>>c;
			gs1[i*2+(c=='1'?1:0)]++;
		}
	}	
	g*=2;
	copy(gs1, &gs1[g], gs);
	compute(s/2);
}

int main(int argc, char** argv){
	cin>>t;
	l(i,t){
		cin>>n>>b>>f;
		l(i,n)
			if((i/16)%2)cout<<'1';
			else cout<<'0';
		cout<<endl;
		{
			char c;
			char l='1';
			g=0;
			l(i,n-b){
				cin>>c;
				if(c!=l){
					l=c;
					gs[++g-1]=1;
				}
				else gs[g-1]++;
			}
		}
		compute(16);
		l(i,n)if(!gs[i])cout<<i<<" ";
		cout<<endl;
		cin>>r;
	}
	return 0;
}
