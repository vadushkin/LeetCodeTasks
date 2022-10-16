class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if (i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0])) or (grid[i][j] != '1'):
            return
        grid[i][j] = ''
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


def main():
    s = Solution()
    print(s.numIslands([
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["1", "0", "0", "0", "1"],
    ]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 470 ms, faster than 55.62% of Python3 online submissions for Number of Islands.
Memory Usage: 16.4 MB, less than 81.99% of Python3 online submissions for Number of Islands.

2. Runtime: 336 ms, faster than 88.14% of Python3 online submissions for Number of Islands.
Memory Usage: 16.5 MB, less than 50.32% of Python3 online submissions for Number of Islands.
"""
