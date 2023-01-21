class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return len({x < y for x, y in zip(nums, nums[1:]) if x != y}) <= 1


def main():
    s = Solution()
    print(s.isMonotonic([1, 2, 3, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1045 ms Beats 68.33%
   Memory 27.9 MB Beats 85.19%

2. Runtime 953 ms Beats 96.95%
   Memory 27.7 MB Beats 95.78%
"""
