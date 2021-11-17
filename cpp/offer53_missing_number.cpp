#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    // 排序数组中的搜索问题，首先想到 二分法 解决
    int missingNumber(vector<int> &nums)
    {
        int n = nums.size();
        if (nums[0] != 0)
        {
            return 0;
        }
        else if (nums[n-1] != n)
        {
            return n;
        }
        int right = n - 1;
        int left = 1;
        int ans = left;
        while (right > left)
        {
            int mid = (right+left)/2;
            if (nums[mid] == mid)
            {
                left = mid + 1;
                ans = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return ans;
    }
};

int main()
{
}