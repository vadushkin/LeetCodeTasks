from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current

        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key=lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k + 1]):
            if i > 0 and x == nums[i - 1]:
                continue
            current = self.KSumClosest(nums[i + 1:], k - 1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest


s = Solution()
print(s.threeSumClosest([1, 2, 3, 4, 5, 1], 10))


"""Tests:
1. Runtime: 139 ms, faster than 99.94% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.3 MB, less than 15.12% of Python3 online submissions for 3Sum Closest.

2. Runtime: 150 ms, faster than 99.76% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.3 MB, less than 15.12% of Python3 online submissions for 3Sum Closest.
"""