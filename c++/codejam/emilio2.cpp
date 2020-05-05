#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv){
	//read all birthdays
	vector<string> birthdays;
	string date;
	while(cin>>date) birthdays.push_back(date);

	//sort birthdays
	sort(birthdays.begin(), birthdays.end());

	//print birthdays without repetition
	for(int i=0; i<birthdays.size(); i++)
		if(i == 0 || birthdays[i].compare(birthdays[i-1]))
			cout<<birthdays[i]<<endl;

	return 0;
}
