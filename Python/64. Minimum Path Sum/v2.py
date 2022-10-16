import itertools


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [path for path in itertools.accumulate(grid[0])]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]


def main():
    s = Solution()
    print(s.minPathSum([[1, 2, 1],
                        [1, 3, 1],
                        [2, 6, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 199 ms, faster than 36.58% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 14.7 MB, less than 97.10% of Python3 online submissions for Minimum Path Sum.

2. Runtime: 89 ms, faster than 99.68% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 14.7 MB, less than 97.10% of Python3 online submissions for Minimum Path Sum.
"""
