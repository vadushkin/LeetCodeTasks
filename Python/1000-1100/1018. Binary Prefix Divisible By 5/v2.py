from itertools import accumulate


class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        return [x % 5 == 0 for x in accumulate(nums, lambda x, y: (x << 1) + y)]


def main():
    s = Solution()
    print(s.prefixesDivBy5([0, 1, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 360 ms Beats 64.46%
   Memory 15.3 MB Beats 28.65%

2. Runtime 345 ms Beats 74.65%
   Memory 15.3 MB Beats 28.65%
"""
