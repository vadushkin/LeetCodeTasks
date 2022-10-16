from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grids[(r // 3, c // 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grids[(r // 3, c // 3)].add(board[r][c])

        return True


def main():
    s = Solution()
    print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
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
1. Runtime: 182 ms, faster than 26.27% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.8 MB, less than 99.12% of Python3 online submissions for Valid Sudoku.

2. Runtime: 103 ms, faster than 90.06% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.8 MB, less than 82.71% of Python3 online submissions for Valid Sudoku.
"""
