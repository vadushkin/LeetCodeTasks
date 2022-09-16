import bisect


class Solution:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


def main():
    s = Solution()
    print(s.search([12, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9], 9))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 543 ms, faster than 13.21% of Python3 online submissions for Binary Search.
Memory Usage: 15.5 MB, less than 73.15% of Python3 online submissions for Binary Search.

2. Runtime: 620 ms, faster than 5.09% of Python3 online submissions for Binary Search.
Memory Usage: 15.4 MB, less than 73.15% of Python3 online submissions for Binary Search.
"""
