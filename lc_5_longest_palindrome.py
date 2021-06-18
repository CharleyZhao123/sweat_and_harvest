class Solution:
    def longestPalindrome1(self, s: str) -> str:
        len_s = len(s)
        # rs = s[::-1]
        # dp = [[0 for i in range(len_s+1)] for j in range(len_s+1)]
        dp = [([0] * (len_s+1)) for i in range(len_s+1)]
        max_l = max_end = 0
        for i in range(len_s):
            for j in range(len_s):
                if s[len_s-1-i] == s[j]:
                    m = dp[i+1][j+1] = dp[i][j] + 1
                    if m > max_l:
                        # 判断是否是严格回文串，避免'aacabdkacaa'的情况
                        if len_s-1-i == j-m+1:
                            max_l = m
                            max_end = j
                else:
                    dp[i+1][j+1] = 0

        return s[max_end+1-max_l:max_end+1]

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2:
            return s

        dp = [([False] * s_len) for _ in range(s_len)]
        max_len = 1
        max_begin = 0
        for j in range(s_len):
            for i in range(0,(j+1)):
                if j == i:
                    dp[i][j] = True
                elif j == (i + 1):
                    if s[i] == s[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if (s[i] == s[j]) and dp[i+1][j-1] == True:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False

                if dp[i][j] == True:
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        max_begin = i

        return s[max_begin:(max_begin+max_len)]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome1("abcddeefdcba"))
