from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        while j < len(nums):
            x = nums[j]
            if x == val:
                nums.remove(x)
                j = 0
            else:
                j += 1
        return len(nums)


"""genius"""
s = Solution()
print(s.removeElement([1, 2, 3, 4, 5, 6, 2, 2, 2], 2))

"""Tests:
1. Runtime: 37 ms, faster than 89.02% of Python3 online submissions for Remove Element.
Memory Usage: 13.8 MB, less than 97.26% of Python3 online submissions for Remove Element.

2. Runtime: 33 ms, faster than 95.37% of Python3 online submissions for Remove Element.
Memory Usage: 13.8 MB, less than 62.86% of Python3 online submissions for Remove Element.
"""