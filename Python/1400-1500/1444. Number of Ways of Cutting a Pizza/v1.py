from functools import lru_cache


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        mod = 10 ** 9 + 7

        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                pre_sum[r][c] = pre_sum[r][c + 1] + pre_sum[r + 1][c] - pre_sum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(slices, row, column):
            if pre_sum[row][column] == 0:
                return 0

            if slices == 0:
                return 1

            ans = 0

            for n_row in range(row + 1, m):
                if pre_sum[row][column] - pre_sum[n_row][column] > 0:
                    ans = (ans + dp(slices - 1, n_row, column)) % mod

            for nc in range(column + 1, n):
                if pre_sum[row][column] - pre_sum[row][nc] > 0:
                    ans = (ans + dp(slices - 1, row, nc)) % mod

            return ans

        return dp(k - 1, 0, 0)


def main():
    s = Solution()
    print(s.ways(["A..", "AAA", "..."], 3))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 206 ms Beats 77.91% 
   Memory 16.1 MB Beats 29.13%

2. Runtime 197 ms Beats 87.13% 
   Memory 16.1 MB Beats 29.13%
"""
