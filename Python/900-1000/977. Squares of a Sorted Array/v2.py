from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] *= A[i]
        A.sort()
        return A


s = Solution()
print(s.sortedSquares([1, 2, 3, 4, 5]))


"""Tests:
1. Runtime: 360 ms, faster than 49.96% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.7 MB, less than 92.86% of Python3 online submissions for Squares of a Sorted Array.

2. Runtime: 212 ms, faster than 98.41% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.8 MB, less than 92.86% of Python3 online submissions for Squares of a Sorted Array.
"""