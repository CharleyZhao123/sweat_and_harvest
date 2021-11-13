# include<iostream>
# include<string>
using namespace std;

class Solution
{
public:
    string reserveLeftWords(string s, int n)
    {
        int length = s.length();
        string tail = s.substr(0, n);
        s = s + tail;
        return s.substr(n, length);
    }

};
int main()
{
    Solution *s = new Solution();
    cout<<s->reserveLeftWords("abcdefg", 3)<<endl;
    return 0;
}
