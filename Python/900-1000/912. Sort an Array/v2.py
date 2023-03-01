class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.insertion_sort(nums)
        return nums

    @staticmethod
    def insertion_sort(nums: list[int]) -> None:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. TLE

2. TLE
"""
