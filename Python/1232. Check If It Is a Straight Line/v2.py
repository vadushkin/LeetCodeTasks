class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x, y in coordinates[2:]:
            if (y2 - y1) * (x - x1) != (x2 - x1) * (y - y1):
                return False

        return True


def main():
    s = Solution()
    print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 152 ms, faster than 10.85% of Python3 online submissions for Check If It Is a Straight Line.
Memory Usage: 14.4 MB, less than 79.79% of Python3 online submissions for Check If It Is a Straight Line.

2. Runtime: 97 ms, faster than 70.43% of Python3 online submissions for Check If It Is a Straight Line.
Memory Usage: 14.4 MB, less than 30.00% of Python3 online submissions for Check If It Is a Straight Line.
"""
