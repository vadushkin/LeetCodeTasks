class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in nums:
            nums[abs(i) - 1] = -abs(nums[abs(i) - 1])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def main():
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 418 ms, faster than 82.91% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.8 MB, less than 88.01% of Python3 online submissions for Find All Numbers Disappeared in an Array.

2. Runtime: 969 ms, faster than 11.79% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 22 MB, less than 76.91% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
