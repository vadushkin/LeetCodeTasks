class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


def main():
    s = Solution()
    print(s.missingNumber([0, 1, 2, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 283 ms, faster than 30.43% of Python3 online submissions for Missing Number.
Memory Usage: 15.3 MB, less than 40.22% of Python3 online submissions for Missing Number.

2. Runtime: 323 ms, faster than 22.01% of Python3 online submissions for Missing Number.
Memory Usage: 15.2 MB, less than 79.61% of Python3 online submissions for Missing Number.
"""
