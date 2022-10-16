from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        for _ in range((2, 0)[len(nums) < 3]):
            nums.remove(max(nums))
        return max(nums)


s = Solution()
print(s.thirdMax([1, 2]))

"""Tests:
1. Runtime: 84 ms, faster than 53.18% of Python3 online submissions for Third Maximum Number.
Memory Usage: 15.5 MB, less than 21.29% of Python3 online submissions for Third Maximum Number.

2. Runtime: 60 ms, faster than 88.09% of Python3 online submissions for Third Maximum Number.
Memory Usage: 15.4 MB, less than 50.10% of Python3 online submissions for Third Maximum Number.
"""