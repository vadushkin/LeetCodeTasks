from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not (1 <= len(nums) <= 10000):
            return []
        for i in range(len(nums)):
            if not (-10000 <= nums[i] <= 10000):
                return []
            nums[i] **= 2
        nums.sort()
        return nums


s = Solution()
print(s.sortedSquares([1, 2, 3, 4]))


"""Tests:
1. Runtime: 247 ms, faster than 86.54% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.6 MB, less than 97.14% of Python3 online submissions for Squares of a Sorted Array.

2. Runtime: 357 ms, faster than 51.07% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.7 MB, less than 92.86% of Python3 online submissions for Squares of a Sorted Array.
"""