from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            if nums[0] >= target:
                return 0
            return 1
        if 1 > len_nums or len_nums > 10000:
            return -1
        if target < -10000 or target > 10000:
            return -1
        for e, i in enumerate(nums):
            if nums[e] < -10000 or nums[e] > 10000:
                return -1
            if i == target or i > target:
                return e
            if e == len_nums - 1:
                return len_nums
            if i < target < nums[e + 1]:
                return e + 1
        return len_nums


s = Solution()
print(s.searchInsert([1, 2, 3, 4, 5, 6, 8], 100))

"""Tests:
1. Runtime: 82 ms, faster than 44.81% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.9 MB, less than 6.45% of Python3 online submissions for Search Insert Position.

2. Runtime: 76 ms, faster than 55.02% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.7 MB, less than 41.44% of Python3 online submissions for Search Insert Position.

3. Runtime: 81 ms, faster than 46.55% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.7 MB, less than 83.19% of Python3 online submissions for Search Insert Position.
"""