#include <iostream>
using namespace std;

class Solution
{
public:
    // n = 0: 1
    // n = 1: 1
    // n >= 2: f(n) = f(n-1) + f(n-2)
    int numWays(int n)
    {
        int i = 1;
        int j = 1;
        if (n == 0)
            return i;
        
        int temp = 0;
        int count = 2;
        while (count <= n)
        {
            count += 1;
            temp = i;
            i = j;
            j = (j + temp) % 1000000007;
        }
        return j;
    }
};

int main()
{
    return 0;
}