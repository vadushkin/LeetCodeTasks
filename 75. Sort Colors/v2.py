class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()


def main():
    s = Solution()
    print(s.sortColors([0, 0, 1, 2, 0, 1, 0, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 62 ms, faster than 36.91% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 15.83% of Python3 online submissions for Sort Colors.

2. Runtime: 33 ms, faster than 95.89% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 64.92% of Python3 online submissions for Sort Colors.
"""
