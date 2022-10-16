from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n, T = list(set(nums)), [float('-inf')] * 3
        for i in n:
            if i > T[0]:
                T = [i, T[0], T[1]]
                continue
            if i > T[1]:
                T = [T[0], i, T[1]]
                continue
            if i > T[2]:
                T = [T[0], T[1], i]
        return T[2] if T[2] != float('-inf') else T[0]


s = Solution()
print(s.thirdMax([1, 1, 3, 1]))


"""Tests:
1. Runtime: 90 ms, faster than 42.99% of Python3 online submissions for Third Maximum Number.
Memory Usage: 15.5 MB, less than 50.10% of Python3 online submissions for Third Maximum Number.

2. Runtime: 94 ms, faster than 36.60% of Python3 online submissions for Third Maximum Number.
Memory Usage: 15.4 MB, less than 50.10% of Python3 online submissions for Third Maximum Number.
"""