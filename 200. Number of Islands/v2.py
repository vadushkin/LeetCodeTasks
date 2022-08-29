class Solution:
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'

                # this code == tuple/list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                sink(i + 1, j)
                sink(i - 1, j)
                sink(i, j + 1)
                sink(i, j - 1)

                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


def main():
    s = Solution()
    print(s.numIslands([
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "1"],
    ]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 473 ms, faster than 54.79% of Python3 online submissions for Number of Islands.
Memory Usage: 16.6 MB, less than 43.61% of Python3 online submissions for Number of Islands.

2. Runtime: 392 ms, faster than 76.44% of Python3 online submissions for Number of Islands.
Memory Usage: 16.7 MB, less than 43.61% of Python3 online submissions for Number of Islands.
"""
