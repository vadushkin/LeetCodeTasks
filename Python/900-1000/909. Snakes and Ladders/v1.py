from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))

        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1

            columns.reverse()

        dist = [-1] * (n * n + 1)
        q = deque([1])
        dist[1] = 0

        while q:
            curr = q.popleft()

            for next_i in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next_i]
                destination = (board[row][column] if board[row][column] != -1 else next_i)

                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)

        return dist[n * n]


def main():
    s = Solution()
    print(s.snakesAndLadders(
        [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 129 ms Beats 66.32%
   Memory 14 MB Beats 31.20%

2. Runtime 263 ms Beats 29.55%
   Memory 14.1 MB Beats 31.20%
"""
