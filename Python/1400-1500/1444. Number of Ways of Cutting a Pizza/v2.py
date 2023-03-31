from functools import cache


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        w = [[[0] * k for _ in range(n)] for _ in range(m)]

        def maxs(table):
            return [next((i for i in range(len(r))[::-1] if r[i] == 'A'), -1) for r in table]

        rightmost, lowest = maxs(pizza), maxs(zip(*pizza))

        @cache
        def has_apple(r, c):
            return pizza[r][c] == 'A' or (r < m - 1 and has_apple(r + 1, c)) or (c < n - 1 and has_apple(r, c + 1))

        for row in range(m)[::-1]:
            for column in range(n)[::-1]:
                w[row][column][0] = int(has_apple(row, column))

                for l in range(1, k):
                    x = 0
                    r1 = row

                    while r1 < m - 1 and rightmost[r1] < column:
                        r1 += 1
                    while r1 < m - 1:
                        r1 += 1
                        x += w[r1][column][l - 1]

                    c1 = column

                    while c1 < n - 1 and lowest[c1] < row:
                        c1 += 1
                    while c1 < n - 1:
                        c1 += 1
                        x += w[row][c1][l - 1]

                    w[row][column][l] = x

        return w[0][0][-1] % (10 ** 9 + 7)


def main():
    s = Solution()
    print(s.ways(["A..", "AAA", "..."], 3))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 149 ms Beats 99.59% 
   Memory 15.1 MB Beats 70.33%

2. Runtime 147 ms Beats 99.59% 
   Memory 15 MB Beats 70.87%
"""
