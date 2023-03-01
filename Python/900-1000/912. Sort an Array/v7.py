class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.bubble_sort(nums)
        return nums

    @staticmethod
    def bubble_sort(nums: list[int]) -> None:
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. TLE

2. TLE
"""
