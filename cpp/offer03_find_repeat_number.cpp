# include<iostream>
# include<unordered_map>
# include<vector>
using namespace std;

class Solution
{
public:
    int findRepeatNumbe(vector<int> &nums)
    {
        unordered_map<int, int> nums_map;
        vector<int>::iterator i;

        for (i=nums.begin(); i<=nums.end(); i++)
        {
            if (nums_map.count(*i) == 1)
            {
                return *i;
            }
            nums_map[*i] = 1;
        }
        return 0;
    }
};

int main()
{
    int a[7] = {1, 2, 3, 4, 3, 5, 7};
    Solution *s = new Solution();
    vector<int> nums(a, a+6);
    cout<<s->findRepeatNumbe(nums);
    return 0;
}
