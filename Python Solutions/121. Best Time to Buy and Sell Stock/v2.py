class Solution:
    def maxProfit(self, prices):
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit


def main():
    s = Solution()
    print(s.maxProfit([2, 45, 4, 1, 1000, 7]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2330 ms, faster than 10.25% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 85.68% of Python3 online submissions for Best Time to Buy and Sell Stock.

2. Runtime: 1141 ms, faster than 88.82% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 85.68% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
