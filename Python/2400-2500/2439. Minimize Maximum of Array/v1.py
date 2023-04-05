from itertools import accumulate


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        return max((num + i) // (i + 1) for i, num in enumerate(accumulate(nums)))


def main():
    s = Solution()
    print(s.minimizeArrayValue([3, 7, 1, 6]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 771 ms Beats 87% 
   Memory 26.8 MB Beats 39.46%

2. Runtime 773 ms Beats 86.10% 
   Memory 26.8 MB Beats 39.46%
"""
