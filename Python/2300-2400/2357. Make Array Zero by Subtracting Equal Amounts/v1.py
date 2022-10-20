class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        j = 0
        while any(nums):
            nums = [i - min(nums, key=lambda x: x == 0) if i != 0 else 0 for i in nums]
            j += 1
        return j


def main():
    s = Solution()
    print(s.minimumOperations([1, 5, 0, 3, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 108 ms, faster than 5.25% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.
Memory Usage: 13.8 MB, less than 96.37% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.

2. Runtime: 104 ms, faster than 5.25% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.
Memory Usage: 13.9 MB, less than 58.08% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.
"""
