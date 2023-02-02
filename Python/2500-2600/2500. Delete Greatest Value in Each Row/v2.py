class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()

        grid = list(zip(*grid))

        return sum(max(row) for row in grid)


def main():
    s = Solution()
    print(s.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 105 ms Beats 81.21% 
   Memory 13.9 MB Beats 57.83%

2. Runtime 91 ms Beats 98.61%
   Memory 14 MB Beats 22.2%
"""
