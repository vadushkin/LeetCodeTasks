class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        low = float("inf")

        for i in prices:
            if low > i:
                low = i

            elif i - low > profit:
                profit = i - low

        return profit


def main():
    s = Solution()
    print(s.maxProfit([4, 1, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 982 ms Beats 88.28% 
   Memory 25.3 MB Beats 5.61%

2. Runtime 930 ms Beats 97.10% 
   Memory 25 MB Beats 82.91%
"""
