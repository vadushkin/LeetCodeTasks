from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                sum_list = nums[i] + nums[s] + nums[e]
                if abs(sum_list - target) < abs(res - target):
                    res = sum_list
                if sum_list < target:
                    s += 1
                else:
                    e -= 1
        return res


s = Solution()
print(s.threeSumClosest([1, 2, 3, 0, 0, -1, -1], 10))

"""Tests:
1. Runtime: 7395 ms, faster than 51.80% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.1 MB, less than 57.66% of Python3 online submissions for 3Sum Closest.

2. Runtime: 7112 ms, faster than 57.72% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.3 MB, less than 15.12% of Python3 online submissions for 3Sum Closest.
"""