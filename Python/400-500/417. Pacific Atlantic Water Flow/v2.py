from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pacific = deque([[0, j] for j in range(n)] + [[i, 0] for i in range(m)])
        atlantic = deque([[i, n - 1] for i in range(m)] + [[m - 1, i] for i in range(n)])

        def bfs(queue):
            visited = set()
            while queue:
                x, y = queue.popleft()
                visited.add((x, y))
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        if (x + dx, y + dy) not in visited:
                            if heights[x + dx][y + dy] >= heights[x][y]:
                                queue.append((x + dx, y + dy))
            return visited

        p, a = bfs(pacific), bfs(atlantic)

        return p.intersection(a)


def main():
    s = Solution()
    print(s.pacificAtlantic([[1, 2, 2, 3, 5],
                             [3, 2, 3, 4, 4],
                             [2, 4, 5, 3, 1],
                             [6, 7, 1, 4, 5],
                             [5, 1, 1, 2, 4]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 881 ms, faster than 11.31% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.5 MB, less than 95.25% of Python3 online submissions for Pacific Atlantic Water Flow.

2. Runtime: 374 ms, faster than 72.66% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.6 MB, less than 78.42% of Python3 online submissions for Pacific Atlantic Water Flow.
"""
