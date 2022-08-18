bisect_left = ...


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        i = bisect_left(range(m), True, key=lambda i: after - i - 1 < 0 or a[i] >= b[after - i - 1])
        nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
        return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0


s = Solution()
print(s.findMedianSortedArrays([1, 23, 4, 5, 6, 7, 89], [1, 2, 3, 4, 5, 6, 8]))

"""Tests: 
1. Runtime: 99 ms, faster than 91.82% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.2 MB, less than 68.01% of Python3 online submissions for Median of Two Sorted Arrays.
 
2. Runtime: 137 ms, faster than 62.30% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14 MB, less than 96.78% of Python3 online submissions for Median of Two Sorted Arrays.
"""