class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i, k in enumerate(nums):
            dif = target - k
            if dif in hash_map:
                return [hash_map[dif], i]
            hash_map[k] = i
        return
