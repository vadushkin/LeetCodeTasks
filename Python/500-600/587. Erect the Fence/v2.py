class Solution:
    def outerTrees(self, points: list[list[int]]) -> list[list[int]]:
        def crossProduct(p1, p2, p3):
            a = p2[0] - p1[0]
            b = p2[1] - p1[1]
            c = p3[0] - p1[0]
            d = p3[1] - p1[1]
            return a * d - b * c

        def constructHalfHull(points):
            stack = []
            for p in points:

                while len(stack) >= 2 and crossProduct(stack[-2], stack[-1], p) > 0:
                    stack.pop()

                stack.append(tuple(p))
            return stack

        points.sort()

        leftToRight = constructHalfHull(points)
        rightToLeft = constructHalfHull(points[::-1])

        return list(set(leftToRight + rightToLeft))


def main():
    s = Solution()
    print(s.outerTrees([[1, 2], [2, 2], [4, 2]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 264 ms Beats 87.95%
   Memory 14.7 MB Beats 89.16%

2. Runtime 730 ms Beats 30.12%
   Memory 14.7 MB Beats 57.83%
"""
