class Solution:
    # 动态规划
    # dp[2] = 1
    # dp[i] = max{dp[i], j * dp[i-j], j * (i-j)} j属于[2, i)
    # 注意：max内需要把dp[i]也带上，用于和之前的结果进行比较
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], j * dp[i-j], j * (i-j))
        return dp[n]

    # 贪心：核心思路是：尽可能把绳子分成长度为3的小段，这样乘积最大
    def cuttingRope1(self, n: int) -> int:
        if n < 4:
            return n - 1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(10))
