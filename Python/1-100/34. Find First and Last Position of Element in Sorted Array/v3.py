import bisect


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect(nums, target) - 1] if target in nums[lo:lo + 1] else [-1, -1]


def main():
    s = Solution()
    print(s.searchRange([1], 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 83 ms Beats 89.17% 
   Memory 15.4 MB Beats 90.33%

2. Runtime 86 ms Beats 80.37% 
   Memory 15.3 MB Beats 90.33%
"""
