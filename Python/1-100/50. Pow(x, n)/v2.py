class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow_n = 1
        while n:
            if n & 1:
                pow_n *= x
            x *= x
            n >>= 1
        return pow_n


s = Solution()
print(s.myPow(2.1, 3))

"""Tests:
1. Runtime: 68 ms, faster than 8.48% of Python3 online submissions for Pow(x, n).
Memory Usage: 13.9 MB, less than 19.97% of Python3 online submissions for Pow(x, n).

2. Runtime: 30 ms, faster than 95.43% of Python3 online submissions for Pow(x, n).
Memory Usage: 13.9 MB, less than 68.53% of Python3 online submissions for Pow(x, n).
"""
