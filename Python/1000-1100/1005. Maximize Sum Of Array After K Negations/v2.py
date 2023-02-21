class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums, i = sorted(nums), k % 2

        while i < len(nums) - 1 and i < k and nums[i] + nums[i + 1] < 0:
            i += 2

        return sum(nums[i:]) - sum(nums[:i])


def main():
    s = Solution()
    print(s.largestSumAfterKNegations([-4, -2, -3], 4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 59 ms Beats 44% 
   Memory 14 MB Beats 46.71%

2. Runtime 50 ms Beats 76.90% 
   Memory 14 MB Beats 11.10%
"""
