from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if 0 > len(nums) or len(nums) > 100:
            return len(nums)
        if 0 > val or val > 100:
            return len(nums)
        for item in nums:
            if item == val:
                nums.remove(val)
        for item in nums:
            if item == val:
                nums.remove(val)
        for item in nums:
            if item == val:
                nums.remove(val)
        for item in nums:
            if item == val:
                nums.remove(val)
        return len(nums)


"""O_O task..."""

s = Solution()
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))


"""Tests:
1. Runtime: 28 ms, faster than 99.00% of Python3 online submissions for Remove Element. O_O
Memory Usage: 14 MB, less than 14.11% of Python3 online submissions for Remove Element.

2. Runtime: 52 ms, faster than 52.73% of Python3 online submissions for Remove Element.
Memory Usage: 13.8 MB, less than 62.86% of Python3 online submissions for Remove Element.
"""