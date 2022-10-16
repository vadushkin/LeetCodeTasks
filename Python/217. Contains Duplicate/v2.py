class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


def main():
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 4, 5, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1134 ms, faster than 5.01% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26.2 MB, less than 28.56% of Python3 online submissions for Contains Duplicate.

2. Runtime: 1390 ms, faster than 5.01% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26.1 MB, less than 28.56% of Python3 online submissions for Contains Duplicate.
"""
