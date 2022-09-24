class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


def main():
    s = Solution()
    print(s.sortColors([0, 0, 0, 1, 1, 2, 2, 0, 0, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 79 ms, faster than 6.33% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 15.83% of Python3 online submissions for Sort Colors.

2. Runtime: 72 ms, faster than 14.51% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 64.92% of Python3 online submissions for Sort Colors.
"""
