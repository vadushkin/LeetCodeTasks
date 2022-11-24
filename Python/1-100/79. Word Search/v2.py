from collections import Counter
from itertools import chain, product


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        if len(word) > m * n:
            return False

        if not (cnt := Counter(word)) <= Counter(chain(*board)):
            return False

        if cnt[word[0]] > cnt[word[-1]]:
            word = word[::-1]

        def dfs(i, j, s):

            if s == len(word):
                return True

            if 0 <= i < m and 0 <= j < n and board[i][j] == word[s]:
                board[i][j] = "#"
                adj = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
                dp = any(dfs(ii, jj, s + 1) for ii, jj in adj)
                board[i][j] = word[s]
                return dp

            return False

        return any(dfs(i, j, 0) for i, j in product(range(m), range(n)))


def main():
    s = Solution()
    print(s.exist([["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], "ABCE"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 95 ms Beats 94.99%
   Memory 13.9 MB Beats 52.49%

2. Runtime 90 ms Beats 95.21%
   Memory 14.1 MB Beats 13.61% 
"""
