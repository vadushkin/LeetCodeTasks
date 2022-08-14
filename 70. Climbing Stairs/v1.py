class Solution:
    def climbStairs(self, n: int) -> int:
        if not (1 <= n <= 45):
            return 0
        if n == 1:
            return 1
        fib1 = fib2 = 1
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib1 + fib2


s = Solution()
print(s.climbStairs(1))

"""Tests:
1. Runtime: 52 ms, faster than 34.08% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 57.10% of Python3 online submissions for Climbing Stairs.

2. Runtime: 47 ms, faster than 48.92% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 57.10% of Python3 online submissions for Climbing Stairs.

3. Runtime: 39 ms, faster than 72.44% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 96.27% of Python3 online submissions for Climbing Stairs.
"""
