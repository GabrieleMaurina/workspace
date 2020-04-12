#define cint unsigned long

#include <iostream>
#include <unordered_set>
#include <queue>
#include <string>
#include <random>

using namespace std;

struct vertex{
	unordered_set<vertex*> neighbors;
	vertex* pair;
	cint dist;
};


struct  bipartite_graph{
	vertex* u;
	vertex* v;
	cint cu;
	cint cv;
	cint ce;

	bipartite_graph(const cint N, const cint E){
		default_random_engine gen(random_device{}());
 		
		cu = uniform_int_distribution<cint>{0, N}(gen);
		cv = N-cu;
		u = new vertex[cu];
		v = new vertex[cv];
		ce = 0;
		uniform_int_distribution<cint> ru(0, cu-1);
		uniform_int_distribution<cint> rv(0, cv-1);
		for(int i=0; i<E; i++){
			cint ur = ru(gen);
			cint vr = rv(gen);
			if(u[ur].neighbors.insert(&v[vr]).second){
				v[vr].neighbors.insert(&u[ur]);
				ce++;
			}
		}
	}

	~bipartite_graph(){
		delete[] u;
		delete[] v;
	}
};

cint hopcroft_karp(const bipartite_graph& bg);
bool bfs(const bipartite_graph& bg, vertex& nil);
bool dfs(vertex& u, const bipartite_graph& bg, const vertex& nil);

int main(const int argc, const char** argv){
	const cint N = (cint)stoll(argv[1]);
	const cint E = (cint)stoll(argv[2]);

	bipartite_graph bg(N, E);

	cout<<"Bipartite graph generated."<<endl<<"|U| = "<<bg.cu<<endl<<"|V| = "<<bg.cv<<endl<<"|E| = "<<bg.ce<<endl;

	cint m = hopcroft_karp(bg);

	cout<<"Hopcroft-Karp algorithm executed."<<endl<<"|M*| = "<<m<<endl;

	return 0;
}

cint hopcroft_karp(const bipartite_graph& bg){
	vertex nil;
	for(int i=0; i<bg.cu; i++) bg.u[i].pair = &nil;
	for(int i=0; i<bg.cv; i++) bg.v[i].pair = &nil;
	cint m = 0;

	while(bfs(bg, nil))
		for(int i=0; i<bg.cu; i++)
			if(bg.u[i].pair == &nil && dfs(bg.u[i], bg, nil))
				m++;

	return m;
}

bool bfs(const bipartite_graph& bg, vertex& nil){
	queue<vertex*> q;

	for(int i=0; i<bg.cu; i++)
		if(bg.u[i].pair == &nil){
			bg.u[i].dist = 0;
			q.push(&bg.u[i]);
		}
		else bg.u[i].dist = bg.ce;
	nil.dist = bg.ce;

	while(!q.empty()){
		vertex& u = *q.front();
		q.pop();
		if(u.dist < nil.dist)
			for(auto v : u.neighbors)
				if(v->pair->dist == bg.ce){
					v->pair->dist = u.dist+1;
					q.push(v->pair);
				}
	}

	return nil.dist != bg.ce;
}

bool dfs(vertex& u, const bipartite_graph& bg, const vertex& nil){
	if(&u != &nil){
		for(auto v : u.neighbors)
			if(v->pair->dist == u.dist+1 && dfs(*v->pair, bg, nil)){
				u.pair = v;
				v->pair = &u;
				return 1;
			}
		u.dist = bg.ce;
		return 0;
	}
	return 1;
}
