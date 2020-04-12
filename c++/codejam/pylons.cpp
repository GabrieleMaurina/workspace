#define cint uint16_t
#define l(i,k) for(cint i=0; i<k; i++)

#include <iostream>
#include <cstdint>
#include <cstdlib>
#include <ctime>

using namespace std;

cint t;
cint g[20][20];
cint p[400][2];
cint r, c, rc;
const cint imp[6][2]={{2,2},{2,3},{2,4},{3,2},{4,2},{3,3}};
const cint impl=6;

void rst(){
	l(i,r)l(j,c)g[i][j]=0;
}

bool f(cint x, cint y){
	if(g[x][y]==rc)return 1;
	l(i,r)l(j,c){
		if(!g[i][j] && i!=x && j!=y && i-j!=x-y && i+j!=x+y){
			g[i][j]=g[x][y]+1;
			p[g[x][y]][0]=i;
			p[g[x][y]][1]=j;
			if(f(i,j))return 1;
			g[i][j]=0;
		}
	}
	return 0;
}

bool fill(){
	rst();
	l(i,r/2+1)l(j,c/2+1){
		g[i][j]=1;
		p[0][0]=i;
		p[0][1]=j;
		if(f(i,j))return 1;
		g[i][j]=0;
	}
	return 0;
}

cint rnd(cint m){
	return (cint)(rand()%m);
}

bool fillr(){
	srand(time(0));
	cint x,y;
	while(1){
		rst();
		l(i,rc){
			x=rnd(r);
			y=rnd(c);
			bool found=0;
			l(j,rc)
				if(i>0 && (g[x][y] || p[i-1][0]==x || p[i-1][1]==y || p[i-1][0]+p[i-1][1]==x+y || p[i-1][0]-p[i-1][1]==x-y)){
					cout<<i<<" "<<x<<" "<<y<<endl;
					if(x<r-1)x++;
					else if(y<c-1){
						x=0;
						y++;
					}
					else{
						x=0;
						y=0;
					}
				}
				else{
					g[x][y]=i>0?g[p[i-1][0]][p[i-1][1]]+1:1;
					p[i][0]=x;
					p[i][1]=y;
					cout<<"asdf "<<g[x][y]<<" "<<i<<endl;
					found==1;
					if(i==rc-1)return 1;
					else break;
				}
			l(a,r){
				l(b,c)cout<<g[a][b]<<" ";
				cout<<endl;
			}
			cout<<endl;
			if(!found)break;
		}
	}
}

bool psb(){
	l(i,impl)
		if(r==imp[i][0] && c==imp[i][1])return 0;
		else if(r==imp[i][1] && c==imp[i][0])return 0;
	return 1;
}

int main(int argc, char** argv){
	cin>>t;
	l(tc,t){
		cin>>r>>c;
		rc=r*c;
		cout<<"Case #"<<tc+1<<": ";
		if(psb()){
			cout<<"POSSIBLE"<<endl;
			if(rc>=25)
				fill();
			else{
				fillr();
			}
			l(i,rc)cout<<p[i][0]+1<<" "<<p[i][1]+1<<endl;
		}
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
