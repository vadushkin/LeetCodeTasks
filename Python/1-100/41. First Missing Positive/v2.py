class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        for i in range(n):
            if abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


def main():
    s = Solution()
    print(s.firstMissingPositive([1, 2, 3, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 184 ms, faster than 100.00% of Python3 online submissions for First Missing Positive.
Memory Usage: 22.2 MB, less than 100.00% of Python3 online submissions for First Missing Positive.

2. Runtime: 371 ms, faster than 99.86% of Python3 online submissions for First Missing Positive.
Memory Usage: 22.2 MB, less than 100.00% of Python3 online submissions for First Missing Positive.
"""
