class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            n = nums[:i] + nums[i + 1:]
            p = path + [nums[i]]
            self.dfs(n, p, res)


s = Solution()
print(s.permute([1, 2, 3]))

"""Tests:
1. Runtime: 50 ms, faster than 77.81% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 58.59% of Python3 online submissions for Permutations.

2. Runtime: 70 ms, faster than 34.97% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 84.57% of Python3 online submissions for Permutations.
"""
