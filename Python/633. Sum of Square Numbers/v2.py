class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cc = int(c ** 0.5)
        left = 0
        right = cc
        while left <= right:
            res = left ** 2 + right ** 2
            if res == c:
                return True
            elif res < c:
                left += 1
            elif res > c:
                right -= 1
        return False


s = Solution()
print(s.judgeSquareSum(5))

"""Tests:
1. Runtime: 496 ms, faster than 32.54% of Python3 online submissions for Sum of Square Numbers.
Memory Usage: 13.8 MB, less than 62.43% of Python3 online submissions for Sum of Square Numbers.

2. Runtime: 592 ms, faster than 24.04% of Python3 online submissions for Sum of Square Numbers.
Memory Usage: 13.8 MB, less than 96.75% of Python3 online submissions for Sum of Square Numbers.

3. Runtime: 542 ms, faster than 28.37% of Python3 online submissions for Sum of Square Numbers.
Memory Usage: 13.7 MB, less than 96.75% of Python3 online submissions for Sum of Square Numbers.
"""
