class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.merge_sort(nums)

        return nums

    def merge_sort(self, nums: list[int]) -> None:
        if len(nums) > 1:
            mid = len(nums) // 2

            left = nums[:mid]
            right = nums[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1978 ms Beats 44.17%
   Memory 22.1 MB Beats 63.69%

2. Runtime 1974 ms Beats 44.54%
   Memory 22.1 MB Beats 57.31%
"""
