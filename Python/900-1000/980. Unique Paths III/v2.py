from functools import cache


class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = NotImplemented
        mask = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] in (-1, 1):
                    mask ^= 1 << i * n + j

        @cache
        def fn(x, y, _mask):
            if grid[x][y] == 2 and _mask == (1 << m * n) - 1:
                return 1

            ans = 0

            for ii, jj in (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y):
                if 0 <= ii < m and 0 <= jj < n:
                    kk = ii * n + jj
                    if not _mask & 1 << kk:
                        ans += fn(ii, jj, _mask ^ 1 << kk)
            return ans

        return fn(*start, mask)


def main():
    s = Solution()
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 60 ms Beats 88.84%
   Memory 16.6 MB Beats 5.47%

2. Runtime 75 ms Beats 76.84%
   Memory 16.7 MB Beats 5.47%
"""
