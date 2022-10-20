class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board:
            return None
        b = []
        lists_changed_indexes = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self.dfs(board, i, j, b)
                    lists_changed_indexes.append(b.copy())
                    b.clear()
        for i in lists_changed_indexes:
            for j in i:
                if j[0] == 0 or j[1] == 0 or j[0] == len(board) - 1 or j[1] == len(board[0]) - 1:
                    for d in i:
                        board[d[0]][d[1]] = "O"
                    break

    def dfs(self, board, i, j, b):
        if (i < 0) or (j < 0) or (i >= len(board)) or (j >= len(board[0])) or (board[i][j] != 'O'):
            return
        board[i][j] = 'X'
        b.append((i, j))
        self.dfs(board, i + 1, j, b)
        self.dfs(board, i - 1, j, b)
        self.dfs(board, i, j + 1, b)
        self.dfs(board, i, j - 1, b)


def main():
    s = Solution()
    print(s.solve([["X", "X", "X", "X"],
                   ["X", "O", "O", "X"],
                   ["X", "X", "O", "X"],
                   ["X", "O", "X", "X"]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 260 ms, faster than 33.79% of Python3 online submissions for Surrounded Regions.
Memory Usage: 56.6 MB, less than 8.71% of Python3 online submissions for Surrounded Regions.

2. Runtime: 204 ms, faster than 64.26% of Python3 online submissions for Surrounded Regions.
Memory Usage: 56.7 MB, less than 8.71% of Python3 online submissions for Surrounded Regions.
"""
