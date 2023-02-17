class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)
