class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)


def main():
    s = Solution()
    print(s.moveZeroes([0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 3, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1476 ms, faster than 9.15% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.6 MB, less than 64.89% of Python3 online submissions for Move Zeroes.

2. Runtime: 2395 ms, faster than 5.00% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.5 MB, less than 96.88% of Python3 online submissions for Move Zeroes.
"""
