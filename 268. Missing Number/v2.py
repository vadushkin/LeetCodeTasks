class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


def main():
    s = Solution()
    print(s.missingNumber([1, 2, 3, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 316 ms, faster than 23.06% of Python3 online submissions for Missing Number.
Memory Usage: 15.2 MB, less than 79.61% of Python3 online submissions for Missing Number.

2. Runtime: 226 ms, faster than 53.07% of Python3 online submissions for Missing Number.
Memory Usage: 15.1 MB, less than 79.61% of Python3 online submissions for Missing Number.
"""
