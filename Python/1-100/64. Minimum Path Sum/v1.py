class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [0] + [float('inf')] * (N - 1)
        for i in range(M):
            dp[0] += grid[i][0]
            for j in range(1, N):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]


def main():
    s = Solution()
    print(s.minPathSum([[1, 3, 1],
                        [1, 5, 1],
                        [4, 2, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 205 ms, faster than 33.32% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 14.6 MB, less than 97.10% of Python3 online submissions for Minimum Path Sum.

2. Runtime: 136 ms, faster than 75.04% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 14.6 MB, less than 99.75% of Python3 online submissions for Minimum Path Sum.
"""
