class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        dy = y1 - y0
        dx = x1 - x0

        xp = dx * y0 - dy * x0

        for x, y in coordinates:
            if dx * y - dy * x != xp:
                return False
        return True


def main():
    s = Solution()
    print(s.checkStraightLine([[2, 4], [2, 5], [2, 8]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 90 ms, faster than 73.67% of Python3 online submissions for Check If It Is a Straight Line.
Memory Usage: 14.4 MB, less than 30.00% of Python3 online submissions for Check If It Is a Straight Line.

2. Runtime: 60 ms, faster than 97.39% of Python3 online submissions for Check If It Is a Straight Line.
Memory Usage: 14.4 MB, less than 79.79% of Python3 online submissions for Check If It Is a Straight Line.
"""
