#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;





struct vertex;
struct edge;

struct vertex
{
	//int id = -1;
	bool used = false;
	int dfs = -1;
	int maxD = -1;
	int sons = 1;
	vector<edge*>* edges;
};

struct edge
{
	//int id = -1;
	int w = -1;
	vertex* v1;
	vertex* v2;
	
	vertex* other(vertex* v)
	{
		return v == v1 ? v2 : v1;
	}
};





vertex** vertices; //array of all vertices
edge** edges; //array of all edges

int N = 0; //number of vertices
int K = 0; //number of test cases

int* ls; //array of ls for each test case

int D = 0; //diameter of the tree

//farthest vertices
vertex* first;
vertex* second;

int* tots; //array of results




void init();
vertex* findFarthest(vertex* v, int* dist, int* maxDist, int index);
void findDistances();
void markLongestPath(vertex* v);
void setMax(vertex* v);
void populateMaxDs();
bool comparator(vertex* v1, vertex* v2);
void solve();
int count(vertex* v, int& l, int& base, int dfs, int& maxD);
void fina();
int countSons(vertex* v);




int main(int argc, char**)
{
	init();
	findDistances();
	sort(vertices, vertices + N, comparator);
	for(int i = 0; i < N; i++)
	{
		vertices[i] -> used = false;
	}
	countSons(vertices[0]);
	solve();
	fina();
	return 0;
}

int countSons(vertex* v)
{
	int tot = 1;
	
	v -> used = true;
	
	for(edge* e : *(v -> edges))
	{
		vertex* v1 = e -> other(v);
		if(!v1 -> used && v1 -> maxD >= v -> maxD)
		{
			tot += countSons(v1);
		}
	}
	
	v -> sons = tot;
	
	return tot;
}

bool comparator(vertex* v1, vertex* v2)
{
	return v1 -> maxD < v2 -> maxD;
}

void solve()
{
	for(int i = 0; i < N; i++)
	{
		vertices[i] -> dfs = -1;
	}
	
	for(int i = 0; i < K; i++)
	{
		int tot = 0;
		int maxD = vertices[N - 1] -> maxD;
		
		for(int j = 0; j < N; j++)
		{
			vertices[j] -> used = false;
		}
		
		for(int j = 0; j < N; j++)
		{
			if(vertices[j] -> maxD > maxD)
			{
				j = N;
			}
			else
			{
				if(!vertices[j] -> used && vertices[j] -> sons > tot)
				{
					int c = count(vertices[j], ls[i], vertices[j] -> maxD, 0, maxD);
					if(c > tot)
					{
						tot = c;
					}
				}
			}
		}
		
		tots[i] = tot;
	}
}

int count(vertex* v, int& l, int& base, int dfs, int& maxD)
{
	int toRtn = 0;
	
	if(v -> dfs == -1)
	{
		v -> dfs = dfs;
		dfs++;
		
		if(v -> maxD == base)
		{
			v -> used = true;
		}
		
		if(v -> maxD >= base && v -> maxD <= base + l)
		{
			//cout << v -> id << "   " << v -> maxD << "   " << l << "   " << base << "   " << v -> dfs << endl;
			
			if(v -> maxD == vertices[N - 1] -> maxD)
			{
				maxD = base;
			}
			
			toRtn++;
		
			for(int i = 0; i < v -> edges -> size(); i++)
			{
				toRtn += count(v -> edges -> at(i) -> other(v), l , base, dfs, maxD);
			}
		}
		
		v -> dfs = -1;
	}
	
	return toRtn;
}

void fina()
{
	fstream fout("output.txt", ios::out);
	for(int i = 0; i < K; i++)
	{
		fout << tots[i] << endl;
	}
	fout.close();
}

void findDistances()
{
	int dist = 0;
	int maxDist = 0;
	
	first = findFarthest(vertices[0], &dist, &maxDist, 0);
	
	dist = 0;
	maxDist = 0;
	
	second = findFarthest(first, &dist, &maxDist, 0);
	
	D = maxDist;
	
	first -> maxD = D;
	second -> maxD = D;
	
	markLongestPath(second);
	
	setMax(first);
	setMax(second);
}

void setMax(vertex* v)
{
	for(int i = 0; i < v -> edges -> size(); i++)
	{
		edge* nextE = v -> edges -> at(i);
		vertex* nextV = nextE -> other(v);
		if(nextV -> maxD == -1)
		{
			if(nextV -> dfs == -2)
			{
				if(v -> maxD - nextE -> w >= D / 2.0)
				{
					nextV -> maxD = v -> maxD - nextE -> w;
					setMax(nextV);
				}
			}
			else
			{
				nextV -> maxD = v -> maxD + nextE -> w;
				setMax(nextV);
			}
		}
	}
}

void markLongestPath(vertex* v)
{
	int index = v -> dfs;
	v -> dfs = -2;
	for(int i = 0; i < v -> edges -> size(); i++)
	{
		vertex* nextV = v -> edges -> at(i) -> other(v);
		if(nextV -> dfs == index - 1)
		{
			markLongestPath(nextV);
		}
	}
}

vertex* findFarthest(vertex* v, int* dist, int* maxDist, int index)
{
	v -> dfs = index;
	v -> used = true;
	
	if(*dist > *maxDist)
	{
		*maxDist = *dist;
	}
	
	vertex* farthest = v;
	int maxD = *maxDist;
	
	for(int i = 0; i < v -> edges -> size(); i++)
	{
		edge* nextE = v -> edges -> at(i);
		vertex* nextV = nextE -> other(v);
		
		if(!nextV -> used)
		{
			*dist += nextE -> w;
			
			vertex* newV = findFarthest(nextV, dist, maxDist, index + 1);
			
			if(*maxDist != maxD)
			{
				maxD = *maxDist;
				farthest = newV;
			}
			
			*dist -= nextE -> w;
		}
	}
	
	v -> used = false;
	
	return farthest;
}

void init()
{
	fstream fin("input.txt", ios::in);
	
	fin >> N;
	
	vertices = new vertex*[N];
	edges = new edge*[N - 1];
	
	for(int i = 0; i < N; i++)
	{
		vertices[i] = new vertex();
		//vertices[i] -> id = i;
		vertices[i] -> used = false;
		vertices[i] -> dfs = -1;
		vertices[i] -> maxD = -1;
		vertices[i] -> edges = new vector<edge*>();
	}
	
	for(int i = 0; i < N - 1; i++)
	{
		int v1;
		int v2;
		int w;
		
		fin >> v1;
		fin >> v2;
		fin >> w;
		
		edges[i] = new edge();
		//edges[i] -> id = i;
		edges[i] -> v1 = vertices[v1];
		edges[i] -> v2 = vertices[v2];
		edges[i] -> w = w;
		
		vertices[v1] -> edges -> push_back(edges[i]);
		vertices[v2] -> edges -> push_back(edges[i]);
	}
	
	fin >> K;
	
	tots = new int[K];
	ls = new int[K];
	
	for(int i = 0; i < K; i++)
	{
		fin >> ls[i];
	}
	
	fin.close();
}
