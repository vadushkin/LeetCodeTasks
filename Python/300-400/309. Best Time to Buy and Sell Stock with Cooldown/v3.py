class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {}  # cache

        def dfs(index: int, is_buying: bool) -> int:
            if index >= len(prices):
                return 0
            if (index, is_buying) in dp:
                return dp[(index, is_buying)]

            cool_down = dfs(index + 1, is_buying)

            if is_buying:
                buy = dfs(index + 1, not is_buying) - prices[index]
                dp[(index, is_buying)] = max(buy, cool_down)
            else:
                sell = dfs(index + 2, not is_buying) + prices[index]
                dp[(index, is_buying)] = max(sell, cool_down)

            return dp[(index, is_buying)]

        return dfs(0, True)


def main():
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 52 ms Beats 81.28% 
   Memory 19.2 MB Beats 13.33%

2. Runtime 100 ms Beats 28.35%
   Memory 19.2 MB Beats 13.33%
"""
