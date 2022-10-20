class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len(set(nums) - {0})


def main():
    s = Solution()
    print(s.minimumOperations([1, 0, 3, 4, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 71.00% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.
Memory Usage: 13.9 MB, less than 58.08% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.

2. Runtime: 35 ms, faster than 94.82% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.
Memory Usage: 13.8 MB, less than 58.08% of Python3 online submissions for Make Array Zero by Subtracting Equal Amounts.
"""
