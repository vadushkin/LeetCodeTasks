class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        def recurse(i, j):
            if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                return grid[i][j]
            if i > len(grid) - 1 or j > len(grid[0]) - 1:
                return float('inf')
            if (i, j) in memo:
                return memo[(i, j)]
            result = grid[i][j] + min(recurse(i + 1, j), recurse(i, j + 1))
            memo[(i, j)] = result
            return result

        memo = {}
        return recurse(0, 0)


def main():
    s = Solution()
    print(s.minPathSum([[1, 2, 3],
                        [1, 4, 1],
                        [1, 8, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 370 ms, faster than 5.08% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 19.9 MB, less than 8.94% of Python3 online submissions for Minimum Path Sum.

2. Runtime: 161 ms, faster than 60.01% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 19.9 MB, less than 8.94% of Python3 online submissions for Minimum Path Sum.
"""
