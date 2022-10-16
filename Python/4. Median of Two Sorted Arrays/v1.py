from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not (0 <= len(nums1) <= 1000) or not (0 <= len(nums2) <= 1000):
            return 0.0
        sort_array = sorted(nums1 + nums2)
        if (len(sort_array) + 1) % 2 == 0:
            return sort_array[len(sort_array) // 2]
        return (sort_array[(len(sort_array) - 1) // 2] + sort_array[len(sort_array) // 2]) / 2


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))

"""Tests:
1. Runtime: 86 ms, faster than 99.28% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.1 MB, less than 68.01% of Python3 online submissions for Median of Two Sorted Arrays.

2. Runtime: 101 ms, faster than 89.84% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.2 MB, less than 68.01% of Python3 online submissions for Median of Two Sorted Arrays.
"""
