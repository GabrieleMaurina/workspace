#define cint int
#define MAX 1000
#define INF 1000000
#define l(i) for(int i=0; i<n; i++)
#include <iostream>

using namespace std;

cint n;
cint g[MAX][MAX];
cint v[MAX];
cint u[MAX];
cint ms[MAX];
cint mt[MAX];
cint ls[MAX];
cint lt[MAX];
cint l[MAX*2];
cint lc=0;
cint p[MAX];
cint pi[MAX];
cint c=0;
cint pth;
cint z=0;

void init_graph(){
	cin>>n;
	l(i)l(j)cin>>g[i][j];
}

void dual_init(){
	l(i){
		u[i]=g[i][0];
		l(j)if(g[i][j]<u[i]) u[i]=g[i][j];
	}
	l(i){
		v[i]=g[i][0]-u[i];
		l(j)if(g[i][j]-u[i]<v[i]) v[i]=g[i][j]-u[i];
	}
}

void primal_init(){
	l(i) ms[i]=mt[i]=-1;
	l(i)l(j)if(g[i][j]-u[i]-v[j]==0 && ms[i]==-1 && mt[i]==-1){
		c++;
		ms[i]=j;
		mt[j]=i;
	}
}

void path_init(){
	l(i)ls[i]=lt[i]=-1;
	l(i){
		p[i]=INF;
		pi[i]=-1;
	}
	l(i)if(ms[i]==-1){
		ls[i]=-2;
		l[lc++]=i;
		l(j)if(lt[j]==-1 && g[i][j]-u[i]-v[j]<p[j]){
			p[j]=g[i][j]-u[i]-v[j];
			pi[j]=i;
		}
	}
}

void label_prop(){
	cint k=l[--lc];
	if(k<MAX)
		l(i)if(lt[i]==-1 && g[k][i]-u[k]-v[i]){
			lt[i]=k;
			l[lc++]=i+MAX;
		}
	else{
		k-=MAX;
		if(mt[k]!=-1){
			if(ls[mt[k]]==-1){
				ls[mt[k]]=k;
				l[lc++]=mt[k];
				l(i)if(lt[i]==-1 && g[mt[k]][i]-u[mt[k]]-v[i]<p[i]){
					p[i]=g[mt[k]][i]-u[mt[k]]-v[i];
					pi[i]=mt[k];
				}
			}
			else pth=k;
		}
	}
}

void dual_iter(){
	cint sig=INF;
	l(i)if(p[i]<sig && lt[i]==-1)sig=p[i];
	l(i)if(ls[i]!=1)u[i]+=sig;
	l(i)if(lt[i]!=1)v[i]-=sig;
		else p[i]-=sig;
	l(i)if(lt[i]==-1 && p[i]==0){
		lt[i]=pi[i];
		l[lc++]=i+MAX;
	}
}

void primal_iter(){
	cint j=pth, i;
	do{
		i=lt[j];
		mt[j]=i;
		ms[i]=j;
		z+=g[i][j];
		c++;
		j=ls[i];
		if(ls[i]>-2){
			z-=g[i][j];
			c--;
		}
	}while(j>-2);
}

void hungarian(){
	init_graph();
	dual_init();
	primal_init();
	while(c<n){
		path_init();
		pth=-1;
		while(pth==-1){
			while(pth==-1 && lc>0)label_prop();
			if(pth==-1)dual_iter();
		}
		primal_iter();
	}
}

int main(int argc, char**argv){
	hungarian();
	return 0;
}
