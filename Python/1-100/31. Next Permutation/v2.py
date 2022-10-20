class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[len(nums) - 1:i - 1:-1]


def main():
    s = Solution()
    print(s.nextPermutation(
        [1, 1, 5, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 83 ms, faster than 17.15% of Python3 online submissions for Next Permutation.
Memory Usage: 13.8 MB, less than 74.85% of Python3 online submissions for Next Permutation.

2. Runtime: 34 ms, faster than 99.66% of Python3 online submissions for Next Permutation.
Memory Usage: 13.9 MB, less than 25.47% of Python3 online submissions for Next Permutation.
"""
