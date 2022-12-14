class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)

        for i in range(len(nums)):
            if i - 1 > 0:
                dp[i] = nums[i] + max(dp[:i - 1])
            else:
                dp[i] = nums[i]

        return max(dp)


def main():
    s = Solution()
    print(s.rob([1, 2, 3, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 35 ms Beats 88.52%
   Memory 13.8 MB Beats 66.57%

2. Runtime 27 ms Beats 98.62%
   Memory 13.9 MB Beats 66.57%
"""
