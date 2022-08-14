import math


# v2.py without math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if not (1 <= num <= 2 ** 31 - 1):
            return False
        print(str(math.sqrt(num))[-1])
        print(str(math.sqrt(num)))
        return False if str(math.sqrt(num))[-1] != '0' else True


s = Solution()
print(s.isPerfectSquare(13))

"""Tests:
1. Runtime: 55 ms, faster than 34.85% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 13.8 MB, less than 57.04% of Python3 online submissions for Valid Perfect Square.

2. Runtime: 54 ms, faster than 37.28% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 13.9 MB, less than 57.04% of Python3 online submissions for Valid Perfect Square.
"""
