class Solution(object):
    def twoSum(self, nums, target):
        for h, i in enumerate(nums):
            for k, j in enumerate(nums):
                if h == k:
                    continue
                if i + j == target:
                    return [h, k]
