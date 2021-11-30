#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    // dp[i] = max{dp[i-1] + nums[i], nums[i]}
    // max = max{dp[i] | i~[0, n-1]}
    int maxSubArray(vector<int> &nums)
    {
        int max = nums[0];
        int before = nums[0];
        for (int i=1; i<nums.size(); i++)
        {
            if (before > 0)
                before += nums[i];
            else
                before = nums[i];
            
            if (before > max)
                max = before;
        }
        return max;
    }
};

int main()
{
    return 0;
}