class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not (-100.0 < x < 100.0):
            return 0.0
        if not (-2 ** 31 <= n <= 2 ** 31 - 1):
            return 0.0
        if not (-10000 <= x ** n <= 10000):
            return 0.0
        return x ** n


s = Solution()
print(s.myPow(2.1, 3))

"""Tests:
1. Runtime: 43 ms, faster than 65.57% of Python3 online submissions for Pow(x, n).
Memory Usage: 13.9 MB, less than 68.53% of Python3 online submissions for Pow(x, n).

2. Runtime: 42 ms, faster than 68.74% of Python3 online submissions for Pow(x, n).
Memory Usage: 13.9 MB, less than 68.53% of Python3 online submissions for Pow(x, n).
"""