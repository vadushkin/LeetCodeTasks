class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if k >= n // 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        globalMax = [0] * n
        for i in range(1, k + 1):
            localMax = 0
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                localMax = max(globalMax[j], localMax + profit)
                globalMax[j] = max(globalMax[j - 1], localMax)
        return globalMax[-1]


def main():
    s = Solution()
    print(s.maxProfit(2, [10, 5, 0, 2, 4, 1, 10, 4, 15, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 199 ms, faster than 55.22% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
Memory Usage: 14 MB, less than 79.28% of Python3 online submissions for Best Time to Buy and Sell Stock IV.

2. Runtime: 208 ms, faster than 51.73% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
Memory Usage: 14 MB, less than 79.28% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
"""
