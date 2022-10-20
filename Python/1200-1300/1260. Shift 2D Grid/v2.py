class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        l, m, n, k = [num for row in grid for num in row], len(grid), len(grid[0]), k % (
                len(grid) * len(grid[0]))
        l = l[-k:] + l[:-k]
        return [l[i * n: i * n + n] for i in range(m)]


def main():
    s = Solution()
    print(s.shiftGrid([[-649, -730], [-827, 613], [882, 2]], 58))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 388 ms, faster than 49.70% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.3 MB, less than 33.78% of Python3 online submissions for Shift 2D Grid.

2. Runtime: 319 ms, faster than 68.15% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.4 MB, less than 15.20% of Python3 online submissions for Shift 2D Grid.
"""
