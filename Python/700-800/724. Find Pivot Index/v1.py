class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        S = sum(nums)
        left_sum = 0

        for i, x in enumerate(nums):
            if left_sum == (S - left_sum - x):
                return i

            left_sum += x

        return -1


def main():
    s = Solution()
    print(s.pivotIndex([-1, -1, 0, 1, 1, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 323 ms Beats 61.88%
   Memory 15.2 MB Beats 92.61%

2. Runtime 161 ms Beats 89.86%
   Memory 15.2 MB Beats 92.61%
"""
