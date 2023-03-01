class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.selection_sort(nums)
        return nums

    @staticmethod
    def selection_sort(nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            _min = min(nums[i:])
            min_index = nums[i:].index(_min)
            nums[i + min_index] = nums[i]
            nums[i] = _min

        return nums


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. TLE

2. TLE
"""
