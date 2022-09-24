class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = nums.count(0), nums.count(1)
        for i in range(len(nums)):
            if a != 0:
                nums[i] = 0
                a -= 1
            elif b != 0:
                nums[i] = 1
                b -= 1
            else:
                nums[i] = 2


def main():
    s = Solution()
    print(s.sortColors([0, 0, 1, 2, 0, 1, 0, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 51 ms, faster than 62.39% of Python3 online submissions for Sort Colors.
Memory Usage: 13.8 MB, less than 64.92% of Python3 online submissions for Sort Colors.

2. Runtime: 72 ms, faster than 14.51% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 15.83% of Python3 online submissions for Sort Colors.
"""
