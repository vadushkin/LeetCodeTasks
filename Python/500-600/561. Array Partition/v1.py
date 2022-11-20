class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        max_sum = 0

        for i in range(0, len(nums), 2):
            max_sum += nums[i]

        return max_sum


def main():
    s = Solution()
    print(s.arrayPairSum([1, 4, 3, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 766 ms Beats 13.66%
   Memory 16.8 MB Beats 21.57%

2. Runtime 287 ms Beats 91.10%
   Memory 16.7 MB Beats 56.64%
"""
