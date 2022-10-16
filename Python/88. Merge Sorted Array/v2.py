from typing import List


class Solution:
    def merge(self, q: List[int], m: int, w: List[int], n: int) -> None:
        a, b, write_index = m - 1, n - 1, m + n - 1

        while b >= 0:
            if a >= 0 and q[a] > w[b]:
                q[write_index] = q[a]
                a -= 1
            else:
                q[write_index] = w[b]
                b -= 1

            write_index -= 1


s = Solution()
print(s.merge([1, 2, 3, 4, 5, 6], 6, [1, 2, 3], 3))

"""Tests:
1. Runtime: 47 ms, faster than 75.76% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.9 MB, less than 85.62% of Python3 online submissions for Merge Sorted Array.

2. Runtime: 86 ms, faster than 5.19% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Merge Sorted Array.
"""
