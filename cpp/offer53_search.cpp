# include<iostream>
# include<vector>
using namespace std;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        if (nums.empty())
        {
            return 0;
        }
        vector<int>::iterator i;
        int n = 0;
        for (i=nums.begin(); i<=nums.end(); i++)
        {
            if (*i == target)
            {
                n += 1;
            }
            if (*i > target)
            {
                break;
            }
        }
        return n;
    }
    int search_(vector<int>& nums, int target)
    {
        if (nums.empty())
        {
            return 0;
        }
        int n = 0;
        for (int i=0; i < nums.size(); i++)
        {
            if (nums[i] == target)
            {
                n += 1;
            }
            if (nums[i] > target)
            {
                break;
            }
        }
        return n;
    }
};

int main()
{
    Solution *s = new Solution();
    vector<int> in(1, 2);
    cout<<s->search(in, 1)<<endl;
}
