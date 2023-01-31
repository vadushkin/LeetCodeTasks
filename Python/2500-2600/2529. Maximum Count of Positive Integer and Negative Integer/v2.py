from bisect import bisect_left


class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        return max(bisect_left(nums, 0), len(nums) - bisect_left(nums, 1))


def main():
    s = Solution()
    print(s.maximumCount([-2, -1, -1, 1, 2, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 135 ms Beats 33.60%
   Memory 14.1 MB Beats 51.44%

2. Runtime 129 ms Beats 65.2% 
   Memory 14.2 MB Beats 51.44%
"""
