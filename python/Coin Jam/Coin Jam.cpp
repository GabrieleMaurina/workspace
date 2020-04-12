#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

uint64_t getFactor(uint64_t number);
void nextAttempt(bool* array , int dim);
uint64_t convertBaseN(bool* array, int dim, int n);
bool isPrime(uint64_t number);


int main(int argc, const char * argv[])
{
    
    int N = 16;
    int J = 50;
    
    bool current_number[N - 2];
    int found = 0;
    fill_n(current_number, N - 2, 0);
    ofstream output("C:\\Users\\Gabriele\\Desktop\\output.txt");
    output << "Case #1:" << endl;
    
    while(found < J)
    {
        bool toContinue = true;
        for(int i = 2; i < 11 && toContinue ; i ++)
        {
            if(isPrime(convertBaseN(current_number, N-2, i)))
            {
                toContinue = false;
            }
        }
        
        if(toContinue)
        {
            output << convertBaseN(current_number, N-2, 10) << " ";
            
            for(int i = 2; i < 11; i ++)
            {
                output << getFactor(convertBaseN(current_number, N-2, i)) << " ";
            }
            
            output << endl;
            found ++;
        }
        
        nextAttempt(current_number, N-2);
    }

    return 0;
}

void nextAttempt(bool* array , int dim)
{
    bool carry = 1;
    for(int i = dim-1; i >=0 && carry; i--)
    {
        if(array[i] == 0)
        {
            array[i]= 1;
            carry = 0;
        }
        else
        {
            array[i]= 0;
        }
    }
}

bool isPrime(uint64_t number)
{
    bool tortn = true;
    for(int i = 2; i <= sqrt(number); i++)
    {
        if((number % i) == 0)
        {
            tortn = false;
            break;
        }
    }
    return tortn;
}

uint64_t convertBaseN(bool* array, int dim, int n)
{
    uint64_t tortn = 1 + pow(n, dim + 1);
    for(int i = 0; i < dim; i ++)
    {
        tortn += pow(array[i] * n, dim - i);
    }
    return tortn;
}

uint64_t getFactor(uint64_t number)
{
    uint64_t tortn = number;
    for(int i = 2; i <= sqrt(number); i++)
    {
        if((number % i) == 0)
        {
            tortn = i;
            break;
        }
    }
    return tortn;
}
