class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and heights[new_x][new_y] >= \
                        heights[x][y]:
                    dfs(visited, new_x, new_y)

        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n - 1)

        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m - 1, j)

        return list(p_visited.intersection(a_visited))


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
1. Runtime: 716 ms, faster than 12.89% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.5 MB, less than 78.42% of Python3 online submissions for Pacific Atlantic Water Flow.

2. Runtime: 466 ms, faster than 47.68% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.6 MB, less than 78.42% of Python3 online submissions for Pacific Atlantic Water Flow.
"""
