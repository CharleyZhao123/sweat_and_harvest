class Solution:
    def numWays(self, n: int) -> int:
        # dp n = dp n - 1 + dp n - 2 
        # n = 0 1
        # n = 1 1
        # n = 2 2
        a, b = 1, 1
        i = 2
        while i <= n:
            a, b = b, a+b
            i += 1
        
        return b%1000000007

if __name__ == '__main__':
    s = Solution()
    print(s.numWays(2))