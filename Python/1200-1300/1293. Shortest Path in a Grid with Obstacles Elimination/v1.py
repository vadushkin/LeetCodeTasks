import collections


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = collections.deque([])

        q.append((0, 0, 0, k))

        seen = set()

        while q:

            r, c, steps, rk = q.popleft()

            if r == rows - 1 and c == cols - 1:
                return steps

            else:
                for y, x in directions:
                    nr = r + y
                    nc = c + x

                    if 0 <= nr < rows and 0 <= nc < cols \
                            and (nr, nc, rk) not in seen:

                        if grid[nr][nc] == 1 and rk > 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk - 1))

                        elif grid[nr][nc] == 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk))

        return -1


def main():
    s = Solution()
    print(s.shortestPath([
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]], 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 556 ms, faster than 50.57% of Python3 online 
submissions for Shortest Path in a Grid with Obstacles Elimination.
Memory Usage: 21.3 MB, less than 41.13% of Python3 online 
submissions for Shortest Path in a Grid with Obstacles Elimination.

2. Runtime: 595 ms, faster than 49.41% of Python3 online 
submissions for Shortest Path in a Grid with Obstacles Elimination.
Memory Usage: 21.2 MB, less than 41.13% of Python3 online 
submissions for Shortest Path in a Grid with Obstacles Elimination.
"""
