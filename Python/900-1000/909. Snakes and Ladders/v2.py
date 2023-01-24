class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        need = {1: 0}
        bfs = [1]

        for x in bfs:
            for i in range(x + 1, x + 7):
                a, b = (i - 1) // n, (i - 1) % n
                nxt = board[-(a + 1)][b if a % 2 == 0 else -(b + 1)]

                if nxt > 0:
                    i = nxt

                if i == n * n:
                    return need[x] + 1

                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1


def main():
    s = Solution()
    print(s.snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 219 ms Beats 37.81%
   Memory 13.9 MB Beats 67.56%

2. Runtime 115 ms Beats 88.64%
   Memory 13.9 MB Beats 67.56%
"""
