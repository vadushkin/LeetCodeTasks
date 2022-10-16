class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


def main():
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 0, 3, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 202 ms, faster than 82.02% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.6 MB, less than 16.58% of Python3 online submissions for Move Zeroes.

2. Runtime: 176 ms, faster than 91.83% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.5 MB, less than 64.89% of Python3 online submissions for Move Zeroes.
"""
