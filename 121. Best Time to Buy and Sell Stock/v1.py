class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        globalMax = [0] * n
        localMax = 0
        for j in range(1, n):
            profit = prices[j] - prices[j - 1]
            localMax = max(globalMax[j], localMax + profit)
            globalMax[j] = max(globalMax[j - 1], localMax)
        return globalMax[-1]


def main():
    s = Solution()
    print(s.maxProfit([4, 1, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1245 ms, faster than 79.84% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 38.43% of Python3 online submissions for Best Time to Buy and Sell Stock.

2. Runtime: 1231 ms, faster than 80.77% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 38.43% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
