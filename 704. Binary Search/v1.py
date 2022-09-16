class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(nums: list[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        return binary_search(nums, target)


def main():
    s = Solution()
    print(s.search([1, 2, 3, 3, 5], 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 555 ms, faster than 11.45% of Python3 online submissions for Binary Search.
Memory Usage: 15.2 MB, less than 99.52% of Python3 online submissions for Binary Search.

2. Runtime: 388 ms, faster than 49.13% of Python3 online submissions for Binary Search.
Memory Usage: 15.6 MB, less than 25.99% of Python3 online submissions for Binary Search.
"""
