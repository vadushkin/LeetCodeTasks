class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x0, y0 = i, j

        res = 0

        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y = x0 + i, y0 + j

            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p':
                    res += 1

                if board[x][y] != '.':
                    break

                x, y = x + i, y + j

        return res


def main():
    s = Solution()
    print(s.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", "p", ".", ".", ".", "."],
                             [".", ".", ".", "R", ".", ".", ".", "p"],
                             [".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", "p", ".", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", "."]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 28 ms Beats 95.95% 
   Memory 13.8 MB Beats 83.81%

2. Runtime 30 ms Beats 92.20%
   Memory 13.9 MB Beats 83.81%
"""
