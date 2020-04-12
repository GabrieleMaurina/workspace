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
	vector<edge*>* edges;
	vector<vertex*>* leaves;
	
	/*void toString()
	{
		cout << "    " << id << " " << maxD << " " << dfs << endl;
	}*/
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
//edge** edges; //array of all edges

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
void fina();





int main(int argc, char**)
{	
	init();
	findDistances();
	sort(vertices, vertices + N, comparator);
	solve();
	fina();
	return 0;
}

bool comparator(vertex* v1, vertex* v2)
{
	return v1 -> maxD > v2 -> maxD;
}

void solve()
{
	for(int i = 0; i < K; i++)
	{
		for(int i = 0; i < N; i++)
		{
			vertices[i] -> used = false;
			vertices[i] -> dfs = 1;
		}
			
		int tot = 0;
		for(int j = 0; j < N; j++)
		{
			vertices[j] -> used = true;
			
			
			
			//Add leaves
			vertices[j] -> leaves -> clear();
			vertices[j] -> leaves -> resize(0);
			
			
			for(int e = 0; e < vertices[j] -> edges -> size(); e++)
			{
				vertex* v = vertices[j] -> edges -> at(e) -> other(vertices[j]);
				if(v -> maxD >= vertices[j] -> maxD && v -> used)
				{
					if(v -> leaves -> size() > 0)
					{
						vertices[j] -> leaves -> insert(vertices[j] -> leaves -> end(), v -> leaves -> begin(), v -> leaves -> end());
					}
					else
					{
						vertices[j] -> leaves -> push_back(v);
					}
					
					v -> leaves -> clear();
					v -> leaves -> resize(0);
					
					vertices[j] -> dfs += v -> dfs;
				}
			}
			
			
			
			//Check leaves
			for(int e = 0; e < vertices[j] -> leaves -> size(); e++)
			{
				vertex* v = vertices[j] -> leaves -> at(e);
				while(v -> maxD > vertices[j] -> maxD + ls[i] && v -> used)
				{
					v -> used = false;
					for(int o = 0; o < v -> edges -> size(); o++)
					{
						vertex* v1 = v -> edges -> at(o) -> other(v);
						if(v1 -> maxD < v -> maxD)
						{
							v = v1;
							break;
						}
					}
					
					vertices[j] -> dfs--;
				}
				
				if(v -> used)
				{
					vertices[j] -> leaves -> at(e) = v;
				}
				else
				{
					vertices[j] -> leaves -> erase(vertices[j] -> leaves -> begin() + e--);
				}
			}
			
			
			//Update tot
			if(vertices[j] -> dfs > tot)
			{
				tot = vertices[j] -> dfs;
			}
		}
		
		tots[i] = tot;
	}
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
	//edges = new edge*[N - 1];
	
	for(int i = 0; i < N; i++)
	{
		vertices[i] = new vertex();
		//vertices[i] -> id = i;
		vertices[i] -> used = false;
		vertices[i] -> dfs = -1;
		vertices[i] -> maxD = -1;
		vertices[i] -> edges = new vector<edge*>(0);
		vertices[i] -> leaves = new vector<vertex*>(0);
	}
	
	for(int i = 0; i < N - 1; i++)
	{
		int v1;
		int v2;
		int w;
		
		fin >> v1;
		fin >> v2;
		fin >> w;
		
		/*edges[i] = new edge();
		edges[i] -> id = i;
		edges[i] -> v1 = vertices[v1];
		edges[i] -> v2 = vertices[v2];
		edges[i] -> w = w;
		
		vertices[v1] -> edges -> push_back(edges[i]);
		vertices[v2] -> edges -> push_back(edges[i]);*/
		
		edge* e = new edge();
		//e -> id = i;
		e -> v1 = vertices[v1];
		e -> v2 = vertices[v2];
		e -> w = w;
		
		vertices[v1] -> edges -> push_back(e);
		vertices[v2] -> edges -> push_back(e);
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
