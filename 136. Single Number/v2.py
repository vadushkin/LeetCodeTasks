class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return sum(list(set(nums))) * 2 - sum(nums)


def main():
    s = Solution()
    print(s.singleNumber([1, 2, 2, 3, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 190 ms, faster than 68.46% of Python3 online submissions for Single Number.
Memory Usage: 17 MB, less than 9.67% of Python3 online submissions for Single Number.

2. Runtime: 323 ms, faster than 18.44% of Python3 online submissions for Single Number.
Memory Usage: 17.1 MB, less than 5.11% of Python3 online submissions for Single Number.
"""
