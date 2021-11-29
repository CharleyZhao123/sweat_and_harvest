#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    // dp[i] = max{dp[i-1], (prices[i] - before_min_price)}
    // 两种选择: 今天i卖, 今天i不卖, 那个利润多选哪个
    // 今天卖: prices[i] - before_min_price
    // 今天不卖: dp[i-1]
    int maxProfit(vector<int> &prices)
    {
        int nums = prices.size();
        if (nums <= 1)
            return 0;
        
        int max_profit = 0;
        int min_price = prices[0];
        int now_profit = 0;
        for (int i=1; i<nums; i++)
        {
            now_profit = prices[i] - min_price;
            if (now_profit > max_profit)
                max_profit = now_profit;
            
            if (prices[i] < min_price)
                min_price = prices[i];
        }

        return max_profit;
    }
};

int main()
{
    return 0;
}