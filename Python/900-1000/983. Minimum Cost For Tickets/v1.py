class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0 for _ in range(days[-1] + 1)]

        for i in range(days[-1] + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 7)] + costs[1], dp[max(0, i - 1)] + costs[0], dp[max(0, i - 30)] + costs[2])

        return dp[-1]


def main():
    s = Solution()
    print(s.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 53 ms Beats 39.96% 
   Memory 13.9 MB Beats 58.35%

2. Runtime 51 ms Beats 47.19% 
   Memory 14 MB Beats 58.35%
"""
