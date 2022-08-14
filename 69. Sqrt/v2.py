class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1


s = Solution()
print(s.mySqrt(4))

"""Tests:
1. Runtime: 62 ms, faster than 53.03% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.8 MB, less than 57.11% of Python3 online submissions for Sqrt(x).

2. Runtime: 67 ms, faster than 44.75% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.8 MB, less than 57.11% of Python3 online submissions for Sqrt(x).

3. Runtime: 68 ms, faster than 43.16% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.8 MB, less than 96.36% of Python3 online submissions for Sqrt(x).
"""
