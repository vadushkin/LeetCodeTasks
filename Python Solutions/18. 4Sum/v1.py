from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        len_array = len(nums)
        result = []
        nums.sort()
        for i in range(len_array - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len_array - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len_array - 1
                while left < right:
                    sum_array = nums[left] + nums[right] + nums[i] + nums[j]
                    if sum_array == target:
                        result.append([nums[left], nums[right], nums[i], nums[j]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum_array < target:
                        left += 1
                    else:
                        right -= 1
        return result


def main():
    s = Solution()
    print(s.fourSum([2, 2, 2, 2, 2], 8))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1593 ms, faster than 39.66% of Python3 online submissions for 4Sum.
Memory Usage: 13.9 MB, less than 63.98% of Python3 online submissions for 4Sum.

2. Runtime: 1642 ms, faster than 37.86% of Python3 online submissions for 4Sum.
Memory Usage: 13.9 MB, less than 63.98% of Python3 online submissions for 4Sum.

3. Runtime: 1787 ms, faster than 33.35% of Python3 online submissions for 4Sum.
Memory Usage: 13.9 MB, less than 63.98% of Python3 online submissions for 4Sum.
"""
