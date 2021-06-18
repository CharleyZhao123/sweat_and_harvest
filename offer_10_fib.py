# 高下立判
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

class Solution2:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = 1
            a, b = 0, 1 
            i = 2
            while i <= n:
                result = a + b
                a, b = b, result
                i += 1
            return result%1000000007