from itertools import accumulate


class Solution:
    def prefixesDivBy5(self, nums: list[int | bool]) -> list[bool]:
        sums = 0

        for i, a in enumerate(nums):
            sums = sums * 2 % 5 + a
            nums[i] = sums % 5 == 0

        return nums


def main():
    s = Solution()
    print(s.prefixesDivBy5([0, 1, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 118 ms Beats 92.29%
   Memory 14.8 MB Beats 98.35%

2. Runtime 109 ms Beats 96.97% 
   Memory 14.7 MB Beats 100%
"""
