class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(board), len(board[0])

        def backtrack(i, j, k, visited):
            if board[i][j] == word[k]:
                if k == len(word) - 1:
                    return True

                for xn, yn in directions:
                    x, y = i + xn, j + yn
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                        visited.add((x, y))

                        if backtrack(x, y, k + 1, visited):
                            return True
                        visited.remove((x, y))
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0, {(i, j)}):
                    return True

        return False


def main():
    s = Solution()
    print(s.exist([["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], "ABCB"))


if __name__ == "__main__":
    main()

"""Tests:
1. Time Limit Exceeded
   50 / 84 testcases passed

2. Runtime 9761 ms Beats 5.1% 
   Memory 14 MB Beats 13.61%
"""
