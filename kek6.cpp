#include <iostream>
using namespace std;
int main()
{
    int fib1 = 0;
    int fib2 = 1;
    double x;
    double a;
    double fib;
    std::cin >> a;
    while (fib2 <= a){
        fib = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib;
        x = fib1+fib2;
    }
    if (a == 2)
    {
        cout << fib2 << endl;
    }
    else {
        
    
    cout << x << endl;
    }
}
