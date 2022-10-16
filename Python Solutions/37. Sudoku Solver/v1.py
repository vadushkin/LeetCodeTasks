class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        assert (self.backtrack(board, 0, 0))
        return

    def backtrack(self, board: list[list[str]], r: int, c: int) -> bool:

        while board[r][c] != '.':
            c += 1
            if c == 9:
                c, r = 0, r + 1
            if r == 9:
                return True

        for k in range(1, 10):
            if self.isValidSudokuMove(board, r, c, str(k)):
                board[r][c] = str(k)
                if self.backtrack(board, r, c):
                    return True
        board[r][c] = '.'
        return False

    def isValidSudokuMove(self, board: list[list[str]], r: int, c: int, cand: int) -> bool:
        if any(board[r][j] == cand for j in range(9)):
            return False
        if any(board[i][c] == cand for i in range(9)):
            return False
        br, bc = 3 * (r // 3), 3 * (c // 3)
        if any(board[i][j] == cand for i in range(br, br + 3) for j in range(bc, bc + 3)):
            return False
        return True


def main():
    s = Solution()
    print(s.solveSudoku([["5", "3", "4", ".", "7", ".", ".", ".", "."],
                         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", "6", "."],
                         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", "6", ".", ".", ".", ".", "2", "8", "."],
                         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 760 ms, faster than 32.43% of Python3 online submissions for Sudoku Solver.
Memory Usage: 14 MB, less than 42.97% of Python3 online submissions for Sudoku Solver.

2. Runtime: 1093 ms, faster than 17.73% of Python3 online submissions for Sudoku Solver.
Memory Usage: 13.9 MB, less than 95.97% of Python3 online submissions for Sudoku Solver.
"""
