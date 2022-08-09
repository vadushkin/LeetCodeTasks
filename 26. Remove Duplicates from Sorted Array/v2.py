from typing import List


class Solution:
    def removeDuplicates(self, nums):
        return list(set(nums))


s = Solution()
print(s.removeDuplicates([1, 2, 34, 1, 1, 2, 3]))


"""Tests:
1. Very Quickly.

2. Very Quickly.
"""