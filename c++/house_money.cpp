#define MAX 20

#define inf "house_money.in"
#define outf "house_money.out"

#define l(i,k) for(int i=0; i<k; i++)

#include<iostream>
#include<fstream>
#include<iomanip>
#include<cmath>

using namespace std;

ifstream in;
ofstream out;

int ppl=0;
char nms[MAX][MAX];
double exps[MAX][MAX];
int e_n[MAX];
double tots[MAX];
double tot;
double each;
double owes[MAX][MAX];
double b[MAX];
double b1[MAX];

void input(const char i[]){
	in.open(i);
	while(in>>nms[ppl]){
		while(in.peek()!='\n'&&in>>exps[ppl][e_n[ppl]])tots[ppl]+=exps[ppl][e_n[ppl]++];
		tot+=tots[ppl];
		ppl++;
	}
	each=tot/ppl;
	l(i,ppl)b[i]=b1[i]=tots[i]-each;
	in.close();
}

int highest(){
	double a=0.01;
	int p=-1;
	l(i,ppl)if(b[i]>a){
		p=i;
		a=b[i];
	}
	return p;
}

int lowest(){
	double a=-0.01;
	int p=-1;
	l(i,ppl)if(b[i]<a){
		p=i;
		a=b[i];
	}
	return p;
}

void compute(){
	int hi,lo;
	double a;
	while((lo=lowest())>-1){
		hi=highest();
		a=min(-b[lo],b[hi]);
		b[lo]+=a;
		b[hi]-=a;
		owes[lo][hi]=a;
	}
}

double r2(double x){
	return round(x*100.0)/100.0;
}

void output(const char o[]){
	out.open(o);
	out<<"Tot:"<<tot<<endl<<"People:"<<ppl<<endl<<"Each:"<<each<<endl<<endl;
	out<<left;
	l(i,ppl){
		out<<setw(20)<<nms[i];
		out<<"Paid:"<<setw(10)<<r2(tots[i]);
		out<<"Balance:"<<setw(10)<<r2(b1[i]);
		out<<"Expenses:";
		l(j,e_n[i])out<<r2(exps[i][j])<<" ";
		out<<endl;
	}
	out<<endl;
	l(i,ppl)if(tots[i]<each){
		out<<setw(20)<<nms[i]<<setw(10)<<"Owes:";
		l(j,MAX)if(owes[i][j])out<<setw(20)<<nms[j]<<setw(10)<<r2(owes[i][j]);
		out<<endl;
	}
	out.close();
}

int main(const int argc, char** argv){
	input(argc==3?argv[1]:inf);
	compute();
	output(argc==3?argv[2]:outf);
	return 0;
}
