class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return set(range(1, len(nums) + 1)) - set(nums)


def main():
    s = Solution()
    print(s.findDisappearedNumbers([1, 3, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 800 ms, faster than 33.05% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 26.9 MB, less than 6.65% of Python3 online submissions for Find All Numbers Disappeared in an Array.

2. Runtime: 344 ms, faster than 97.53% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 26.9 MB, less than 6.65% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
