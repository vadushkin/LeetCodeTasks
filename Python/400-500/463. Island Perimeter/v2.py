import operator


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        return sum(sum(map(operator.ne, [0] + row, row + [0])) for row in grid + list(map(list, zip(*grid))))


def main():
    s = Solution()
    print(s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 477 ms Beats 89.62% 
   Memory 14.2 MB Beats 68.49%

2. Runtime 459 ms Beats 95.64% 
   Memory 14.2 MB Beats 89.88%
"""
