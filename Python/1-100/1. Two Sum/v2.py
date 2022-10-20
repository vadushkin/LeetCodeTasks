class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) > 10000 or len(nums) < 2 or target > 100000000 or target < -100000000:
            return
        hash_map = {}
        for i, k in enumerate(nums):
            if k > 100000000 or k < -100000000:
                return
            dif = target - k
            if dif in hash_map:
                return [hash_map[dif], i]
            hash_map[k] = i
        return


s = Solution()
s.twoSum([2, 7, 11, 15], 9)

"""Tests:
1. Runtime: 64 ms, faster than 77.60% of Python online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 68.38% of Python online submissions for Two Sum.

2. Runtime: 37 ms, faster than 99.07% of Python online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 44.80% of Python online submissions for Two Sum.
"""
