class Solution(object):
    def isPerfectSquare(self, num):
        if num < 0:
            return False
        x, i = 0, 1
        while x < num:
            x += i
            i += 2
        return x == num


s = Solution()
print(s.isPerfectSquare(16))

"""Tests:
1. Runtime: 51 ms, faster than 45.43% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 13.9 MB, less than 57.04% of Python3 online submissions for Valid Perfect Square.

2. Runtime: 75 ms, faster than 8.60% of Python3 online submissions for Valid Perfect Square. O_O
Memory Usage: 13.8 MB, less than 96.59% of Python3 online submissions for Valid Perfect Square.

3. Runtime: 65 ms, faster than 16.31% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 13.9 MB, less than 57.04% of Python3 online submissions for Valid Perfect Square.
"""
