class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            dp[i] = min(dp[i + 1:i + nums[i] + 1]) + 1 if nums[i] > 0 else float("inf")

        return dp[0]


def main():
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 706 ms Beats 37.29% 
   Memory 14.9 MB Beats 98.58%

2. Runtime 698 ms Beats 37.48% 
   Memory 15 MB Beats 89.52%
"""
