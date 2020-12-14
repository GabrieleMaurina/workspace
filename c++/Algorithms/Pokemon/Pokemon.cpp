	#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct vertex;
struct edge;
struct group;



struct vertex
{
	vector<edge*>* edges;
	int index;
	vertex* twin;
};

struct edge
{
	vertex* v1;
	vertex* v2;
	int index;
	bool bridge;
	bool simplified;
	int pokemon;
	edge* twin;
};

struct group
{
	vector<edge*>* edges;
	int size;
};

int N = 0;
int M = 0;
int K = 0;

vertex* vertices;
edge* edges;



vector<group>* groups;
bool* visited;
vector<edge*>** subGroups;


//Tarjan
int cnt;
int* pre;
int* low;



fstream fin("input.txt", ios::in);
fstream fout("output.txt", ios::out);



void init();
void fina();
int GCD(int first, int second);
void tarjan();
void dfs(int u, int v);
vertex* getOtherVertex(vertex* v, edge* e);
edge* getOtherEdge(vertex* v, edge* e);
int sizeOfConnected(vertex* v);
int dfsSize(vertex* v);
void makeGroups();
int edgesNotBridges(vertex* v);
void placePokemon();
void findK();
void simplifyGraph();
void explore(bool* checked, vertex* v);



int main(int argc, char** argv)
{
	init();
	tarjan();
	simplifyGraph();
	makeGroups();
	findK();
	placePokemon();
	fina();
	return 0;
}

void placePokemon()
{
	for(int i = 0; i < groups -> size(); i++)
	{
        int c = 0;
		for(int j = 0; j < groups -> at(i).edges -> size(); j++)
		{
            for(int l = 0; l < subGroups[groups -> at(i).edges -> at(j) -> twin -> index] -> size(); l++)
            {
                    subGroups[groups -> at(i).edges -> at(j) -> twin -> index] -> at(l) -> pokemon = c % K;
                    c++;
            }
		}
	}
}

void findK()
{
	for(int i = 0; i < groups -> size(); i++)
	{
        int tot = 0;
        for(int j = 0; j < groups -> at(i).edges -> size(); j++)
        {
                tot += subGroups[groups -> at(i).edges -> at(j) -> twin -> index] -> size();
        }
		K = GCD(K, tot);
	}
}

void explore(bool* checked, vertex* v)
{
	for(int i = 0; i < v -> edges -> size(); i++)
	{
		edge* e = v -> edges -> at(i);
		if(!checked[e -> index] && !e -> bridge)
		{
			vertex* vNext = v;
			edge* eNext = e;
			int counter = 0;
			do
			{
				subGroups[e -> index] -> push_back(eNext);
				
				if(counter > 0)
				{
                     eNext -> simplified = true;
                } 
				
				vNext = getOtherVertex(vNext, eNext);
				checked[eNext -> index] = true;
				eNext = getOtherEdge(vNext, eNext);
				counter++;
				
			} while(vNext != v && edgesNotBridges(vNext) < 3);
			edge* newE = new edge();
			newE -> v1 = v -> twin;
			newE -> v2 = vNext -> twin;
			newE -> twin = e;
			newE -> bridge = false;
			newE -> simplified = false;
			e -> twin = newE;
			v -> twin -> edges -> push_back(newE);
			vNext -> twin -> edges -> push_back(newE);
		}
	}
}

void simplifyGraph()
{
	vector<vertex*>* crossings = new vector<vertex*>();	
	bool* checked = new bool[M];
	
	for(int i = 0; i < N; i++)
	{
		if(edgesNotBridges(&vertices[i]) > 2)
		{
            vertex* v = new vertex();
            v -> edges = new vector<edge*>();
            v -> index = vertices[i].index;
            v -> twin = &vertices[i];
            vertices[i].twin = v;
			crossings -> push_back(&vertices[i]);
		}
	}
	
	for(int i = 0; i < M; i++)
	{
		checked[i] = edges[i].bridge;
	}
	
	for(int i = 0; i < crossings -> size(); i++)
	{
		explore(checked, crossings -> at(i));
	}
	
	for(int i = 0; i < M; i++)
	{
		if(!checked[i])
		{
            vertex* v = new vertex();
            v -> edges = new vector<edge*>();
            v -> index = edges[i].v1 -> index;
            v -> twin = edges[i].v1;
            edges[i].v1 -> twin = v;
			explore(checked, edges[i].v1);
		}
	}
}

void makeGroups()
{
	for(int i = 0; i < M; i++)
	{
		if(!edges[i].bridge && !edges[i].simplified)
		{
			bool found = false;
			int g = 0;
			for(int j = 0; j < groups -> size() && !found; j++)
			{
				edges[i].twin -> bridge = true;
				groups -> at(j).edges -> at(0) -> bridge = true;
				
				if(sizeOfConnected(groups -> at(j).edges -> at(0) -> v1) != groups -> at(j).size)
				{
					found = true;
					g = j;
				}
				
				edges[i].twin -> bridge = false;
				groups -> at(j).edges -> at(0) -> bridge = false;
			}
			
			if(found)
			{
				groups -> at(g).edges -> push_back(edges[i].twin);
			}
			else
			{
				group* gr = new group();
				gr -> size = sizeOfConnected(edges[i].twin -> v1);
				gr -> edges = new vector<edge*>();
				gr -> edges -> push_back(edges[i].twin);
				groups -> push_back(*gr);
			}
		}
	}
}

int edgesNotBridges(vertex* v)
{
	int tot = 0;
	
	for(int i = 0; i < v -> edges -> size(); i++)
	{
		if(!v -> edges -> at(i) -> bridge)
		{
			tot++;
		}
	}
	
	return tot;
}

int sizeOfConnected(vertex* v)
{
	for(int i = 0; i < N; i++)
	{
		visited[i] = false;
	}
	
	return dfsSize(v);
}

int dfsSize(vertex* v)
{
	visited[v -> index] = true;
	int tot = 1;
	for(int i = 0; i < v -> edges -> size(); i++)
	{
		edge* e = v -> edges -> at(i);
		vertex* next = getOtherVertex(v, e);
		if(!e -> bridge && !visited[next -> index])
		{
			tot += dfsSize(next);
		}
	}
	return tot;
}

vertex* getOtherVertex(vertex* v, edge* e)
{
	return e -> v1 == v ? e -> v2 : e -> v1;
}

edge* getOtherEdge(vertex* v, edge* e)
{
	int i = 0;
	while(v -> edges -> at(i) == e || v -> edges -> at(i) -> bridge)
	{
		i++;
	}
	return v -> edges -> at(i);
}

void tarjan()
{
    for (int v = 0; v < N; v++)
    {
    	if (pre[v] == -1)
    	{
            dfs(v, v);
		}
	}
}

void dfs(int u, int v)
{
    pre[v] = cnt++;
    low[v] = pre[v];
    
    for(int i = 0; i < vertices[v].edges -> size(); i++)
    {
    	edge* e = vertices[v].edges->at(i);
    	int w = getOtherVertex(&vertices[v], e) -> index;
        if (pre[w] == -1)
		{
            dfs(v, w);
            low[v] = low[v] < low[w] ? low[v] : low[w];
            if (low[w] == pre[w])
			{
                e -> bridge = true;
            }
        }
        else if (w != u)
        {
            low[v] =low[v] < pre[w] ? low[v] : pre[w];
		}
	}
}

int GCD(int first, int second)
{
    while (second != 0)
	{
        int r = first % second;
        first = second;
        second = r;
    }
    return first;
}

void init()
{
	fin >> N;
    fin >> M;
	
	vertices = new vertex[N];
	edges = new edge[M];
	visited = new bool[N];
	groups = new vector<group>();
	subGroups = new vector<edge*>*[M];
	
	for(int i = 0; i < N; i++)
	{
		vertices[i].index = i;
        vertices[i].edges = new vector<edge*>();
    }
    
	for(int i = 0; i < M; i++)
	{
        int first, second;
        
        
        fin >> first;
        fin >> second;
        
        
        edges[i].index = i;
        edges[i].bridge = false;
        edges[i].simplified = false;
        edges[i].pokemon = 0;
        edges[i].v1 = &vertices[first];
        edges[i].v2 = &vertices[second];
        
        
        vertices[first].edges->push_back(&edges[i]);
        vertices[second].edges->push_back(&edges[i]);
        
        
        subGroups[i] = new vector<edge*>();
    }
    
    low = new int[N];
    pre = new int[N];
    
    for (int i = 0; i < N; i++) low[i] = -1;
    for (int i = 0; i < N; i++) pre[i] = -1;
}

void fina()
{
	fout << K << endl;
    for(int i = 0; i< M; i++)
	{
        fout << edges[i].pokemon << endl;
    }
	
	fin.close();
	fout.close();
}
