class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binarySearchLeft(a, x):
            left, right = 0, len(a) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > a[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binarySearchRight(a, x):
            left, right = 0, len(a) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= a[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return [left, right] if left <= right else [-1, -1]


def main():
    s = Solution()
    print(s.searchRange([1, 2, 3, 4, 5, 6, 7, 8], 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 117 ms, faster than 67.99% of Python3 online submissions for Find First and L Pos of Element in Sort. Array.
Memory Usage: 15.5 MB, less than 9.42% of Python3 online submissions for Find First and L Pos of Element in Sort. Array.

2. Runtime: 213 ms, faster than 5.20% of Python3 online submissions for Find First and L Pos of Element in Sort. Array.
Memory Usage: 15.4 MB,less than 47.96% of Python3 online submissions for Find First and L Pos of Element in Sort. Array.
"""
