class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m = len(board)
        n = len(board[0])
        res = []

        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        ref = set()
        for i in range(m):
            for j in range(n - 1):
                ref.add(board[i][j] + board[i][j + 1])

        for j in range(n):
            for i in range(m - 1):
                ref.add(board[i][j] + board[i + 1][j])

        for word in words:
            f = True
            for i in range(len(word) - 1):
                if word[i:i + 2] not in ref and word[i + 1] + word[i] not in ref:
                    f = False
                    break
            if not f:
                continue
            if self.findWord(word, m, n, board, d):
                res.append(word)
        return res

    def findWord(self, word, m, n, board, d) -> bool:
        if word[:4] == word[0] * 4:
            word = ''.join([c for c in reversed(word)])

        starts = []
        stack = []
        visited = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    starts.append((i, j))

        for start in starts:
            stack.append(start)
            visited.add((start,))
            b = 1

            while stack != [] and b < len(word):
                x, y = stack[-1]
                for dxy in d:
                    nx, ny = x + dxy[0], y + dxy[1]
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == word[b]:
                            if (nx, ny) not in stack and tuple(stack) + ((nx, ny),) not in visited:
                                stack.append((nx, ny))
                                visited.add(tuple(stack))
                                b += 1
                                if b == len(word):
                                    return True
                                break
                else:
                    stack.pop()
                    b -= 1
        else:
            return False


def main():
    s = Solution()
    print(s.findWords([["o", "a", "a", "n"],
                       ["e", "t", "a", "e"],
                       ["i", "h", "k", "r"],
                       ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 143 ms Beats 98.88%
   Memory 14.2 MB Beats 99.12%
2. Runtime 148 ms Beats 98.86%
   Memory 14.4 MB Beats 97.87%
"""
