class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)


s = Solution()
print(s.combinationSum([1, 2, 3], 3))
"""Tests:
1. Runtime: 124 ms, faster than 57.88% of Python3 online submissions for Combination Sum.
Memory Usage: 13.8 MB, less than 99.37% of Python3 online submissions for Combination Sum.

2. Runtime: 132 ms, faster than 52.20% of Python3 online submissions for Combination Sum.
Memory Usage: 14 MB, less than 92.76% of Python3 online submissions for Combination Sum.

3. Runtime: 97 ms, faster than 80.45% of Python3 online submissions for Combination Sum.
Memory Usage: 13.9 MB, less than 92.76% of Python3 online submissions for Combination Sum.
"""
