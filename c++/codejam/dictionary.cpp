#include <iostream>
#include <unordered_map>

using namespace std;

int main(int argc, char** argv){
	string word;
	string definition;
	unordered_map<string, string> dictionary;

	//read number of words
	int n;
	cin>>n;
	cin.ignore(1,'\n');

	//fill dictionary
	for(int i=0; i<n; i++){
		getline(cin, word, ',');
		getline(cin, definition);
		dictionary[word] = definition;
	}

	//read word queries and print definitions
	while(cin>>word){
		if(dictionary.find(word) == dictionary.end()) definition = "-";
		else definition = dictionary[word];
		cout<<word<<":"<<definition<<endl;
	}

	return 0;
}
