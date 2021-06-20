class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1
            k = quickMul(N//2)
            return k * k if N % 2 == 0 else k * k * x

        return quickMul(n) if n >= 0 else 1.0/quickMul(-n)


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.1, 3))
