from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        mid = l + (h - l) // 2
        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid
            else:
                h = mid
            if h == l + 1:
                break
        if target < nums[l] or target == nums[l]:
            mid = l
        elif target > nums[h]:
            mid = h + 1
        else:
            mid = h
        return mid


s = Solution()
print(s.searchInsert([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))

"""Tests:
1. Runtime: 72 ms, faster than 61.56% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.8 MB, less than 6.45% of Python3 online submissions for Search Insert Position.

2. Runtime: 58 ms, faster than 83.66% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.7 MB, less than 41.44% of Python3 online submissions for Search Insert Position.

3. Runtime: 91 ms, faster than 29.03% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.6 MB, less than 83.19% of Python3 online submissions for Search Insert Position.
"""