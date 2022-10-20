from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


s = Solution()
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

"""Tests:
1. Runtime: 862 ms, faster than 26.32% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 27.1 MB, less than 24.80% of Python3 online submissions for Kth Largest Element in an Array.

2. Runtime: 739 ms, faster than 32.74% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 27.1 MB, less than 33.17% of Python3 online submissions for Kth Largest Element in an Array.
"""