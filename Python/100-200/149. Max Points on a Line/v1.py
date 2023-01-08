from collections import defaultdict


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def line(p1, p2):
            if p2[0] - p1[0] == 0:
                return p1[0]

            slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            b = p1[1] - slope * p1[0]

            return slope, "%.5f" % b

        res = 0

        for i in range(len(points)):
            count = defaultdict(int)

            for j in range(i + 1, len(points)):
                count[line(points[i], points[j])] += 1

            if count:
                res = max(res, max(count.values()))

        return res + 1


def main():
    s = Solution()
    print(s.maxPoints([[1, 1], [2, 2], [3, 3]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 98 ms Beats 85.12% 
   Memory 13.9 MB Beats 75.79%

2. Runtime 105 ms Beats 82.37%
   Memory 13.9 MB Beats 94.26%
"""
