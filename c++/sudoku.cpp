#define l(i) for(int i=0;i<9;i++)

#include <iostream>
#include <fstream>

using namespace std;

char s[9][9];

void input(const char* file){
	ifstream in(file);
	l(i)l(j){
		in>>s[i][j];
		s[i][j]-='0';
	}
	in.close();
}

void output(const char* file){
	ofstream out(file);
	l(i){
		l(j)out<<s[i][j];
		out<<endl;
	}
	out.close();
}

bool solve(const int p){
	int i=p/9;
	int j=p%9;
	while(s[i][j]){
		if(j<8)j++;
		else if(i<8){
			j=0;
			i++;
		}
		else return 1;
	}
	l(k){
		s[i][j]=k;
		if(solve(p+1)) return 1;
	}
	s[i][j]=0;
	return 0;
}

int main(const int argc, const char** argv){
	if(argc == 3){
		input(argv[1]);
		if(solve(0))output(argv[2]);
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
