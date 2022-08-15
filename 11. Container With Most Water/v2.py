class Solution:
    def maxArea(self, height):
        if not (2 <= len(height) <= 100000):
            return 0
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res, h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res


s = Solution()
print(s.maxArea([1, 2, 3, 5]))


"""Tests:
1. Runtime: 1115 ms, faster than 51.09% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.4 MB, less than 54.47% of Python3 online submissions for Container With Most Water.

2. Runtime: 1387 ms, faster than 20.78% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.4 MB, less than 54.47% of Python3 online submissions for Container With Most Water.
"""