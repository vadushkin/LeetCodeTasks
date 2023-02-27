from typing import Optional


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Optional['Node']:
        if not grid:
            return None

        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)

        n = len(grid)

        return Node('*',
                    False,
                    self.construct([row[:n // 2] for row in grid[:n // 2]]),
                    self.construct([row[n // 2:] for row in grid[:n // 2]]),
                    self.construct([row[:n // 2] for row in grid[n // 2:]]),
                    self.construct([row[n // 2:] for row in grid[n // 2:]]))

    def isLeaf(self, grid):
        return all(grid[i][j] == grid[0][0] for i in range(len(grid)) for j in range(len(grid[i])))


def main():
    s = Solution()
    print(s.construct([[0, 1], [1, 0]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 122 ms Beats 55.92% 
   Memory 14.8 MB Beats 41.32%

2. Runtime 113 ms Beats 80.17% 
   Memory 14.7 MB Beats 69.97%
"""
