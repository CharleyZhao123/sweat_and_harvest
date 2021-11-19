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
    
    int binary_search(vector<int> nums, int target, bool lower)
    {
        int size = nums.size();
        int left = 0;
        int right = size-1;
        int mid;
        int ans=right-1;
        // lower: 寻找第一个target
        // mid = t: right = mid
        // mid < t: left = mid + 1
        // mid > t: right = mid
        // higher: 寻找第一个大于target的值
        // mid = t: left = mid + 1
        // mid < t: left = mid + 1
        // mid > t: right = mid
        while (left<right)
        {
            mid = (left+right)/2;
            if (nums[mid]>target || (lower && nums[mid]==target))
            {
                right = mid;
                ans = mid;
            }
            else
            {
                left = mid + 1;
            }
        }
        return ans;
    }

    int search_binary(vector<int> nums, int target)
    {
        int left = binary_search(nums, target, true);
        int right = binary_search(nums, target, false);

        if (nums[right] == target)
            return right - left + 1;
        else
            return right - left;
    }
};

int main()
{
    Solution *s = new Solution();
    vector<int> in(1, 2);
    cout<<s->search(in, 1)<<endl;
}
