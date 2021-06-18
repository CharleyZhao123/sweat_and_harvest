class Solution:
    def longestCommonSubstring(self, s1: str, s2: str):
        len_s1 = len(s1)
        len_s2 = len(s2)
        dp = [([0] * (len_s1+1)) for i in range (len_s2+1)]
        max = 0
        s_end = 0
        for i in range(1, (len_s2+1)):
            for j in range(1, (len_s1+1)):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] > max:
                    max = dp[i][j]
                    s_end = j-1
        max_css = ''
        while max > 0:
            max_css += s1[s_end-max+1]
            max -= 1
        return max_css

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubstring('abccdefgcd', 'gcbccdabc'))