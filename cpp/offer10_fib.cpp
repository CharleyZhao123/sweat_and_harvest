#include <iostream>
using namespace std;

class Solution
{
public:
    int fib(int n)
    {
        int i = 0;
        int j = 1;
        if (n==0)
            return i;
        
        int k = 2;
        int temp = 0;
        while (k<=n)
        {
            k ++;
            temp = i;
            i = j;
            j = j + temp;
            j = j % 1000000007;
        }
        return j;
    }
};

int main()
{
    Solution *s = new Solution();
    cout<<s->fib(2)<<endl;
    return 0;
}