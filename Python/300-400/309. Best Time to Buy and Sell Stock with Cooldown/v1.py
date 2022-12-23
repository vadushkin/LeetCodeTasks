class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cool_down, sell, hold = 0, 0, -float('inf')

        for stock_price_of_day in prices:
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold

            cool_down = max(prev_cool_down, prev_sell)
            sell = prev_hold + stock_price_of_day
            hold = max(prev_hold, prev_cool_down - stock_price_of_day)

        return max(sell, cool_down)


def main():
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 38 ms Beats 97.56% 
   Memory 14.1 MB Beats 97.92%

2. Runtime 39 ms Beats 96.70% 
   Memory 14.1 MB Beats 97.92%
"""
