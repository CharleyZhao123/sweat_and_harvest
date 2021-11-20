#include <iostream>
#include <unordered_map>
#include <string>
#include <queue>
using namespace std;

class Solution
{
public:
    char firstUniqChar1(string s)
    {
        unordered_map<char, int> char_count;
        for (int i=0; i<s.length(); i++)
        {
            if (char_count.count(s[i]))
                char_count[s[i]] += 1;
            else
                char_count[s[i]] = 1;
        }
        for (int i=0; i<s.length(); i++)
            if (char_count[s[i]] == 1)
                return s[i];
        return ' ';
    }
    char firstUniqChar(string s)
    {
        queue<char> char_queue;
        unordered_map<char, int> char_map;
        for (int i=0; i<s.size(); i++)
        {
            if (char_map.count(s[i]))
            {
                char_map[s[i]] += 1;
                while (!char_queue.empty())
                {
                    int front_nums = char_map[char_queue.front()];
                    if (front_nums > 1)
                        char_queue.pop();
                    else
                        break;
                }
            }
            else
            {
                char_map[s[i]] = 1;
                char_queue.push(s[i]);
            }
        }
        if (char_queue.empty())
            return ' ';
        else
            return char_queue.front();
    }
};

int main()
{
    string s = "loveleetcode";
    Solution *so = new Solution();
    cout<<so->firstUniqChar(s)<<endl;
    return 0;
}