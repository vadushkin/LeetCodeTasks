from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n in [0, 1]:
            return [nums]

        if n == 2:
            return [nums, nums[::-1]]

        res = []

        for i in range(n):
            permutations = self.permute(nums[:i] + nums[i + 1:])
            for p in permutations:
                res.append([nums[i]] + p)

        return res


s = Solution()
print(s.permute([1, 2, 3]))

"""Tests:
1. Runtime: 91 ms, faster than 5.86% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 22.97% of Python3 online submissions for Permutations.

2. Runtime: 47 ms, faster than 84.27% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 22.97% of Python3 online submissions for Permutations.
"""