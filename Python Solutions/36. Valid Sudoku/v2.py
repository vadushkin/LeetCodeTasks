class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return all(len(set(x)) == len(x) for x in (
        *[[x for x in y if x != '.'] for y in board], *[[x for x in y if x != '.'] for y in zip(*board)],
        *[[board[i + m][j + n] for m in range(3) for n in range(3) if board[i + m][j + n] != '.'] for i in (0, 3, 6) for
          j in (0, 3, 6)]))


def main():
    s = Solution()
    print(s.isValidSudoku([["5", "4", ".", ".", "7", ".", ".", ".", "."],
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
1. Runtime: 105 ms, faster than 87.79% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.9 MB, less than 35.14% of Python3 online submissions for Valid Sudoku.

2. Runtime: 132 ms, faster than 67.44% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.7 MB, less than 99.12% of Python3 online submissions for Valid Sudoku.

3. Runtime: 107 ms, faster than 85.75% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.9 MB, less than 82.71% of Python3 online submissions for Valid Sudoku.
"""
