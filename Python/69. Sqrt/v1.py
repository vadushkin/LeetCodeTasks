import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if not (0 <= x <= 2 ** 31 - 1):
            return 0
        return int(math.sqrt(x))


s = Solution()
print(s.mySqrt(4))

"""Tests:
1. Runtime: 33 ms, faster than 97.54% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.8 MB, less than 57.11% of Python3 online submissions for Sqrt(x).

2. Runtime: 57 ms, faster than 61.61% of Python3 online submissions for Sqrt(x).
Memory Usage: 14 MB, less than 10.89% of Python3 online submissions for Sqrt(x).

3. Runtime: 48 ms, faster than 77.70% of Python3 online submissions for Sqrt(x).
Memory Usage: 14 MB, less than 10.89% of Python3 online submissions for Sqrt(x).
"""
