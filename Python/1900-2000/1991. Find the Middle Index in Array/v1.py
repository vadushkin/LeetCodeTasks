class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        S = sum(nums)
        left_sum = 0

        for i, x in enumerate(nums):
            if left_sum == (S - left_sum - x):
                return i

            left_sum += x

        return -1


def main():
    s = Solution()
    print(s.findMiddleIndex([2, 3, -1, 8, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 84 ms Beats 41.61%
   Memory 13.8 MB Beats 96.65%

2. Runtime 48 ms Beats 85.61%
   Memory 13.8 MB Beats 61.23%
"""
