class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(map(max, grid + list(zip(*grid)))) + sum(v > 0 for row in grid for v in row)
