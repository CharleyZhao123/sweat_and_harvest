class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1_len = len(text1)
        t2_len = len(text2)
        max_len = 0
        dp = [([0] * (t1_len+1)) for _ in range(t2_len+1)]
        for i in range(1, t2_len+1):
            for j in range(1, t1_len+1):
                if text2[i-1] == text1[j-1]:
                    m = dp[i][j] = dp[i-1][j-1] + 1
                    if m > max_len:
                        max_len = m
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return max_len

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence('abcde', 'agce'))