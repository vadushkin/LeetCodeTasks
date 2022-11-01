from functools import cache


class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])

        @cache
        def helper(r, c):

            if r == m:
                return c

            elif grid[r][c] == 1 and c + 1 < n and grid[r][c + 1] == 1:
                return helper(r + 1, c + 1)

            elif grid[r][c] == -1 and 0 <= c - 1 and grid[r][c - 1] == -1:
                return helper(r + 1, c - 1)

            else:
                return -1

        return [helper(0, j) for j in range(n)]


def main():
    s = Solution()
    print(s.findBall([
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1],
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 203 ms, faster than 93.68% of Python3 online submissions for Where Will the Ball Fall.
Memory Usage: 19 MB, less than 5.19% of Python3 online submissions for Where Will the Ball Fall.

2. Runtime: 256 ms, faster than 81.00% of Python3 online submissions for Where Will the Ball Fall.
Memory Usage: 19.2 MB, less than 5.19% of Python3 online submissions for Where Will the Ball Fall.
"""
