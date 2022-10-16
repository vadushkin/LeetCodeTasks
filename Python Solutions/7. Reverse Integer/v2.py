class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        reversedNumber = 0
        while x:
            reversedNumber = reversedNumber * 10 + x % 10
            x //= 10
        if reversedNumber >= 2 ** 31 - 1 or reversedNumber <= -2 ** 31:
            return 0
        return -reversedNumber if isNegative else reversedNumber


s = Solution()
s.reverse(123123123123123)

"""Tests:
1. Runtime: 46 ms, faster than 66.42% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.8 MB, less than 63.35% of Python3 online submissions for Reverse Integer.

2. Runtime: 71 ms, faster than 9.44% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 16.04% of Python3 online submissions for Reverse Integer.
"""
