#define l(i,k) for(int i=0; i<k; i++)

#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>

using namespace std;

void primMST(int **g,int *p, const int V){
	vector<int> key;
	bool mst[V];
	l(i,V){
		key[i]=INT_MAX;
		mst[i]=false;
	}
	key[0]=0;
	p[0]=-1;
	make_heap(key.begin(), key.end());
	l(i,V-1){
		int mk=pop_heap(key.begin(),key.end());
		mst[mk]=true;
		key.pop_back();
		l(j,V)if(g[mk][j]&&!mst[j]&&g[mk][j]<key[j])p[j]=mk,key[j]=g[mk][j];
	}
}

int main(const int argc, const char **argv){
	return 0;
}
