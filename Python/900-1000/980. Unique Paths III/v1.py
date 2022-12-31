class Solution:
    def __init__(self):
        self.res = 0

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n, empty = len(grid), len(grid[0]), 1
        x = y = NotImplemented

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    empty += 1

        def dfs(_x, _y, _empty):
            if not (0 <= _x < m and 0 <= _y < n and grid[_x][_y] >= 0):
                return

            if grid[_x][_y] == 2:
                self.res += _empty == 0
                return

            grid[_x][_y] = -2

            dfs(_x + 1, _y, _empty - 1)
            dfs(_x - 1, _y, _empty - 1)
            dfs(_x, _y + 1, _empty - 1)
            dfs(_x, _y - 1, _empty - 1)

            grid[_x][_y] = 0

        dfs(x, y, empty)

        return self.res


def main():
    s = Solution()
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 41 ms Beats 99.68%
   Memory 13.9 MB Beats 93.68%

2. Runtime 48 ms Beats 97.58% 
   Memory 13.9 MB Beats 93.68%
"""
