#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int minArray1(vector<int> &nums)
    {
        for (int i=1; i<nums.size(); i++)
        {
            if (nums[i]<nums[i-1])
                return nums[i];
        }
        return nums[0];
    }
    int minArray(vector<int> &numbers)
    {
        int i = 0;
        int j = numbers.size() - 1;

        while (i<j)
        {
            int m = i + (j-i)/2;
            if (numbers[m] > numbers[j])
                i = m + 1;
            else if (numbers[m] < numbers[j])
                j = m;
            else
            {
                int x = i;
                for (int k=i+1; k<=j; k++)
                {
                    if (numbers[k]<numbers[x])
                        x = k;
                }
                return numbers[x];
            }
        }
        return numbers[i];
    }
};

int main()
{
    return 0;
}