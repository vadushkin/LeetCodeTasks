import collections


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        start_row, start_col = entrance
        maze[start_row][start_col] = "+"

        queue = collections.deque()
        queue.append([start_row, start_col, 0])

        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()

            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]

                if 0 <= next_row < rows and 0 <= next_col < cols \
                        and maze[next_row][next_col] == ".":

                    if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:
                        return curr_distance + 1

                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])

        return -1


def main():
    s = Solution()
    print(s.nearestExit([["+", "."]], [0, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2258 ms Beats 25.82%
   Memory 14.5 MB Beats 86.37%

2. Runtime 1849 ms Beats 59.47%
   Memory 14.6 MB Beats 68.60%
"""
