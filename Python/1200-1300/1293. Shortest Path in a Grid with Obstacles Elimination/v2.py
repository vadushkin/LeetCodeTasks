class Solution(object):
    def __init__(self):
        self.rst = None

    def search(self, cur: int, i: int, j: int,
               grid: list[list[int]], k: int) -> None:
        if i < 0 or j < 0 or i > len(grid) - 1 \
                or j > len(grid[0]) - 1:
            return

        if k == 0 and grid[i][j] == 1:
            return

        if grid[i][j] == 2:
            return

        if self.rst == len(grid) + len(grid[0]) - 2:
            return

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            self.rst = min(self.rst, cur)
            return

        c = grid[i][j]
        grid[i][j] = 2

        if c == 1:
            k -= 1

        self.search(cur + 1, i + 1, j, grid, k)
        self.search(cur + 1, i, j + 1, grid, k)
        self.search(cur + 1, i - 1, j, grid, k)
        self.search(cur + 1, i, j - 1, grid, k)

        grid[i][j] = c

    def shortestPath(self, grid: list[list[int]], k: int) -> int:

        self.rst = float('inf')
        self.search(0, 0, 0, grid, k)

        return self.rst if self.rst != float('inf') else -1


def main():
    s = Solution()
    print(s.shortestPath([
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]], 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Time Limit Exceeded
23 / 52 test cases passed.

2. Time Limit Exceeded
23 / 52 test cases passed.
"""
