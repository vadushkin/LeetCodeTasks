class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m, n, perimeter = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                perimeter += 4 * grid[i][j]

                if i > 0:
                    perimeter -= grid[i][j] * grid[i - 1][j]
                if j > 0:
                    perimeter -= grid[i][j] * grid[i][j - 1]

                if i < m - 1:
                    perimeter -= grid[i][j] * grid[i + 1][j]
                if j < n - 1:
                    perimeter -= grid[i][j] * grid[i][j + 1]

        return perimeter


def main():
    s = Solution()
    print(s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 585 ms Beats 63.72% 
   Memory 14.2 MB Beats 89.88%

2. Runtime 595 ms Beats 60.99% 
   Memory 14.2 MB Beats 68.49%
"""
