from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @cache
        def dp(n):
            if n < 2:
                return cost[n]

            return cost[n] + min(dp(n - 1), dp(n - 2))

        length = len(cost)
        return min(dp(length - 1), dp(length - 2))


def main():
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 77 ms Beats 14.71% 
   Memory 16.6 MB Beats 5.9%

2. Runtime 66 ms Beats 39.99% 
   Memory 16.7 MB Beats 5.9%
"""
