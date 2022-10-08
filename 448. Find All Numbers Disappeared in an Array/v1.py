class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return set(range(1, max(nums) if len(nums) < max(nums) else len(nums) + 1)) - set(nums)


def main():
    s = Solution()
    print(s.findDisappearedNumbers([1, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 797 ms, faster than 33.35% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 26.9 MB, less than 6.65% of Python3 online submissions for Find All Numbers Disappeared in an Array.

2. Runtime: 764 ms, faster than 37.39% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 26.9 MB, less than 6.65% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
