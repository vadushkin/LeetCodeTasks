import itertools


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        return max(0.5 * abs(xa * yb + xb * yc + xc * ya - xb * ya - xc * yb - xa * yc)
                   for (xa, ya), (xb, yb), (xc, yc) in itertools.combinations(points, 3))


def main():
    s = Solution()
    print(s.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 236 ms, faster than 60.59% of Python3 online submissions for Largest Triangle Area.
Memory Usage: 13.9 MB, less than 27.93% of Python3 online submissions for Largest Triangle Area.

2. Runtime: 195 ms, faster than 75.00% of Python3 online submissions for Largest Triangle Area.
Memory Usage: 13.9 MB, less than 27.93% of Python3 online submissions for Largest Triangle Area.
"""
