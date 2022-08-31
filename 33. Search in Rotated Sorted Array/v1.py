class Solution:
    def search(self, nums, target):
        try:
            return nums.index(target)
        except:
            return -1


def main():
    s = Solution()
    print(s.search([1, 2, 3, -2, 5], 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 53 ms, faster than 74.89% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.2 MB, less than 91.11% of Python3 online submissions for Search in Rotated Sorted Array.

2. Runtime: 68 ms, faster than 44.76% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.3 MB, less than 55.75% of Python3 online submissions for Search in Rotated Sorted Array.
"""
