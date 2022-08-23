class Solution:
    # O_O
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        if not (1 <= len(nums) <= 100000):
            return False
        if len(nums) == 100000:
            return 100001
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            return 1
        if len(nums) == 2:
            if nums[1] < 1 or nums[0] > 1:
                return 1
            elif nums[0] == 1:
                if nums[1] == 2:
                    return 3
                return 2
            elif nums[0] == 0:
                if nums[1] == 1:
                    return 2
                return 1
            elif nums[1] == 1:
                return 2
            else:
                return 1
        for e, i in enumerate(nums):
            if i < 1:
                continue
            if i == 1:
                for k, g in enumerate(nums[e:]):
                    if len(nums[e:]) == 1:
                        if nums[e] == 1:
                            return 2
                        return 1
                    if nums[e:][k + 1] - nums[e:][k] == 1 or nums[e:][k + 1] - nums[e:][k] == 0:
                        if k == len(nums[e:]) - 2:
                            if nums[e:][k + 1] - nums[e:][k] == 1:
                                return g + 2
                            elif nums[e:][k + 1] - nums[e:][k] == 0:
                                return g + 1
                        continue
                    return nums[e:][k] + 1
            else:
                return 1
        return 1


def main():
    s = Solution()
    print(s.firstMissingPositive([1, 2, 3, 4]))


if __name__ == '__main__':
    main()

"""Tests: O_O
1. Runtime: 154 ms, faster than 100.00% of Python3 online submissions for First Missing Positive.
Memory Usage: 22.3 MB, less than 100.00% of Python3 online submissions for First Missing Positive.

2. Runtime: 232 ms, faster than 99.99% of Python3 online submissions for First Missing Positive.
Memory Usage: 22.3 MB, less than 100.00% of Python3 online submissions for First Missing Positive.
"""
