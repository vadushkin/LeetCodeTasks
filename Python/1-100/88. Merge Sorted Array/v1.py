from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = nums1[:m]
        for i in nums2:
            nums1.append(i)
        nums1.sort()


s = Solution()
print(s.merge([1, 2, 3, 4, 5, 6], 6, [1, 2, 3], 3))


"""Tests:
1. Runtime: 71 ms, faster than 21.80% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.8 MB, less than 85.62% of Python3 online submissions for Merge Sorted Array.

2. Runtime: 54 ms, faster than 60.50% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.8 MB, less than 85.62% of Python3 online submissions for Merge Sorted Array.
"""