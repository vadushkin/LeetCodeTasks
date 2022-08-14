class Solution:
    def fib(self, N: int) -> int:
        if not (0 <= N <= 30): return 0
        a, b = 0, 1
        for i in range(N): a, b = b, a + b
        return a


s = Solution()
print(s.fib(3))


"""Tests:
1. Runtime: 56 ms, faster than 44.52% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 53.92% of Python3 online submissions for Fibonacci Number.

2. Runtime: 50 ms, faster than 57.19% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 53.92% of Python3 online submissions for Fibonacci Number.

3. Runtime: 35 ms, faster than 88.72% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.6 MB, less than 99.75% of Python3 online submissions for Fibonacci Number.

4. Runtime: 35 ms, faster than 88.72% of Python3 online submissions for Fibonacci Number.
Memory Usage: 14 MB, less than 9.49% of Python3 online submissions for Fibonacci Number.
"""