#include <iostream>

using namespace std;

int main(int argc, char** argv){
	//read integer
	int l;
	cin>>l;

	//read list of strings
	string list[l];
	for(int i=0; i<l; i++) cin>>list[i];

	//compare items in store with items in list
	string item;
	int found = 0;
	while(cin>>item){
		for(int i=0; i<l; i++)
			if(!list[i].compare(item)){
				found++;
				break;
			}
	}

	//output result
	cout<<found<<endl;
	return 0;
}
