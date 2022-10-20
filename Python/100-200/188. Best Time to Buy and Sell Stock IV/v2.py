class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if k == 0:
            return 0
        dp = [[1000, 0] for _ in range(k + 1)]
        for price in prices:
            for i in range(1, k + 1):
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        return dp[k][1]


def main():
    s = Solution()
    print(s.maxProfit(2, [2, 10, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 229 ms, faster than 45.27% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
Memory Usage: 13.8 MB, less than 95.05% of Python3 online submissions for Best Time to Buy and Sell Stock IV.

2. Runtime: 291 ms, faster than 32.16% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
Memory Usage: 13.7 MB, less than 99.73% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
"""
