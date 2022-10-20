from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return list(map(list, res))


s = Solution()
print(s.threeSum([1, 2, -1, -1, 0, 0, 0]))

"""Tests:
1. Runtime: 747 ms, faster than 92.53% of Python3 online submissions for 3Sum.
Memory Usage: 18.1 MB, less than 72.13% of Python3 online submissions for 3Sum.

2. Runtime: 978 ms, faster than 76.71% of Python3 online submissions for 3Sum.
Memory Usage: 18.1 MB, less than 72.13% of Python3 online submissions for 3Sum.
"""