#include <iostream>
#include <vector>
using namespace std;

// C++中, 大部分是[ , )区间
// .end()指向的是最后一个元素的后一个位置
int main()
{
    vector<int> a = {1, 2, 3, 4, 5};
    vector<int>::iterator a_it;
    reverse(a.begin(), a.end()-1);
    for (a_it=a.begin(); a_it != a.end(); a_it++)
        cout<<*a_it<<endl;
    

    return 0;
}
