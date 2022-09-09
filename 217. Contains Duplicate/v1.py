class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        return False


def main():
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 4, 5, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1044 ms, faster than 5.75% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26 MB, less than 68.60% of Python3 online submissions for Contains Duplicate.

2. Runtime: 1129 ms, faster than 5.01% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.9 MB, less than 68.60% of Python3 online submissions for Contains Duplicate.
"""
