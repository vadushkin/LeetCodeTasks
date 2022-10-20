class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        if not grid:
            return []

        len_square = len(grid[0])

        square = [number for cell in grid for number in cell]

        if len(square) == k:
            return grid

        ans = []

        if k > len(grid) * len_square:
            k %= len(grid) * len_square

        square = square[-k:] + square[:-k]

        for cell in range(len(grid)):
            slot = []

            for number in range(len_square):
                slot.append(square[number])

            ans.append(slot)
            square = square[len_square:]

        return ans


def main():
    s = Solution()
    print(s.shiftGrid([[-649, -730], [-827, 613], [882, 2]], 58))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 358 ms, faster than 59.83% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.3 MB, less than 33.78% of Python3 online submissions for Shift 2D Grid.
 
2. Runtime: 420 ms, faster than 41.13% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.4 MB, less than 33.78% of Python3 online submissions for Shift 2D Grid.
"""
