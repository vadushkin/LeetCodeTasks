class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return sum((prices[idx + 1] - prices[idx]) for idx in range(len(prices) - 1) if prices[idx] < prices[idx + 1])


def main():
    s = Solution()
    print(s.maxProfit([4, 2, 3, 4, 0, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 128 ms, faster than 19.28% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15.2 MB, less than 69.34% of Python3 online submissions for Best Time to Buy and Sell Stock II.

2. Runtime: 151 ms, faster than 7.25% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15.2 MB, less than 69.34% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Next challenges:"""
