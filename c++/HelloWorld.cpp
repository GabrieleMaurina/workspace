#include <iostream>
#include <tuple>

using namespace std;

int main(int argc, char** argv){
	cout << "Hello World!" << endl;
	tuple<int, int> t = {1, 2};
	cout << get<0>(t) << endl;
}
