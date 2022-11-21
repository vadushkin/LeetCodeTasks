from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        M, N = len(maze), len(maze[0])
        queue, visited = deque([tuple(entrance + [0])]), set(tuple(entrance))

        while queue:
            x, y, d = queue.popleft()

            if ([x, y] != entrance) and (x == 0 or x == M - 1 or y == 0 or y == N - 1):
                return d

            for r, c in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
                if 0 <= r < M and 0 <= c < N and maze[r][c] == '.' and (r, c) not in visited:
                    queue.append((r, c, d + 1))
                    visited.add((r, c))
        return -1


def main():
    s = Solution()
    print(s.nearestExit([["+", "+", ".", "+"],
                         [".", ".", ".", "+"],
                         ["+", "+", "+", "."]], [1, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 823 ms Beats 89.93%
   Memory 15.6 MB Beats 26.78%

2. Runtime 2505 ms Beats 11.72%
   Memory 15.6 MB Beats 26.78%
"""
