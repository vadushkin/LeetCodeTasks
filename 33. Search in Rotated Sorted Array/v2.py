class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


def main():
    s = Solution()
    print(s.search([1, 2, 3, -2, 5], 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 61 ms, faster than 59.25% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.2 MB, less than 55.75% of Python3 online submissions for Search in Rotated Sorted Array.

2. Runtime: 107 ms, faster than 5.48% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.3 MB, less than 55.75% of Python3 online submissions for Search in Rotated Sorted Array.
"""
