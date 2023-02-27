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
        # Fun
        return Node(val=bool(grid[0][0]), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None) \
            if all([all([i == grid[0][0] for i in j]) for j in grid]) \
            else Node(val=bool(grid[0][0]), isLeaf=False,
                      topLeft=self.construct(
                          [[grid[i][j] for j in range(len(grid) // 2)] for i in range(len(grid) // 2)]),
                      topRight=self.construct(
                          [[grid[i][j] for j in range(len(grid) // 2, len(grid))] for i in range(len(grid) // 2)]),
                      bottomLeft=self.construct(
                          [[grid[i][j] for j in range(len(grid) // 2)] for i in range(len(grid) // 2, len(grid))]),
                      bottomRight=self.construct([[grid[i][j] for j in range(len(grid) // 2, len(grid))] for i in
                                                  range(len(grid) // 2, len(grid))])
                      )


def main():
    s = Solution()
    print(s.construct([[0, 1], [1, 0]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 142 ms Beats 25.34% 
   Memory 14.6 MB Beats 86.50%

2. Runtime 135 ms Beats 31.68% 
   Memory 14.8 MB Beats 41.32%
"""
