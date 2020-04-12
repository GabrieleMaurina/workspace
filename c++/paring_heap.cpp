#include <vector>

using namespace std;

template <typename T> class paring_heap{
	protected:
		T value;
		vector<paring_heap<T>> children;
		static paring_heap<T>* merge_pairs(pairing_heap<T> *a){}
	public:
		paring_heap(const T& _value){value=_value;}
		
		static T top(paring_heap<T> *a){return a?a.value:nullptr;}
		static paring_heap<T>* merge(paring_heap<T> *a, paring_heap<T> *b){}
		static paring_heap<T>* insert(paring_heap<T> *a, const T& value){}
		static paring_heap<T>* remove_top(paring_heap<T> *a){}
		static paring_heap<T>* decrease_key(paring_heap<T> *a){}
};
