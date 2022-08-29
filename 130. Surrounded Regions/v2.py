class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not any(board):
            return

        m, n = len(board), len(board[0])
        save = [ij for k in range(m + n) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]


def main():
    s = Solution()
    print(s.solve(
        [["O", "O", "O", "O", "X", "X"],
         ["O", "O", "O", "O", "O", "O"],
         ["O", "X", "O", "X", "O", "O"],
         ["O", "X", "O", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "O"],
         ["O", "X", "O", "O", "O", "O"]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 262 ms, faster than 32.90% of Python3 online submissions for Surrounded Regions.
Memory Usage: 15.4 MB, less than 85.55% of Python3 online submissions for Surrounded Regions.

2. Runtime: 183 ms, faster than 75.10% of Python3 online submissions for Surrounded Regions.
Memory Usage: 15.2 MB, less than 98.14% of Python3 online submissions for Surrounded Regions.
"""
