class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [10000, 0]
        for price in prices:
            dp[0] = min(dp[0], price - dp[1])
            dp[1] = max(dp[1], price - dp[0])
        return dp[1]


def main():
    s = Solution()
    print(s.maxProfit([5, 2, 4, 0, 5, 8, 1]))


if __name__ == "__main__":
    main()

"""Tests;
1. Runtime: 175 ms, faster than 5.09% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15.2 MB, less than 69.34% of Python3 online submissions for Best Time to Buy and Sell Stock II.

2. Runtime: 138 ms, faster than 12.73% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15.1 MB, less than 69.34% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""
