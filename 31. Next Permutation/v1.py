class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                j = i - 1
                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                        nums[k], nums[j] = nums[j], nums[k]
                        return nums
        return nums.reverse()


def main():
    s = Solution()
    print(s.nextPermutation(
        [1, 1, 5, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 54 ms, faster than 75.02% of Python3 online submissions for Next Permutation.
Memory Usage: 13.9 MB, less than 25.47% of Python3 online submissions for Next Permutation.

2. Runtime: 75 ms, faster than 32.17% of Python3 online submissions for Next Permutation.
Memory Usage: 13.8 MB, less than 74.85% of Python3 online submissions for Next Permutation.
"""
