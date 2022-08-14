class Solution:
    def fib(self, n: int) -> int:
        if not(0 <= n <= 30):
            return 0
        if n == 0:
            return 0
        fib1 = fib2 = 1
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2


s = Solution()
print(s.fib(2))


"""Tests:
1. Runtime: 65 ms, faster than 32.19% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 95.62% of Python3 online submissions for Fibonacci Number.

2. Runtime: 27 ms, faster than 97.96% of Python3 online submissions for Fibonacci Number. O_O
Memory Usage: 13.8 MB, less than 95.62% of Python3 online submissions for Fibonacci Number. O_O
"""