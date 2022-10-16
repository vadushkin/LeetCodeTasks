import math


class Solution:
    def largestTriangleArea(self, p: list[list[int]]) -> float:
        L, A = len(p), 0
        for i in range(L - 2):
            for j in range(i + 1, L - 1):
                for k in range(j + 1, L):
                    R = self.area_heron(p[i], p[j], p[k])
                    A = max(A, R)
        return A

    @staticmethod
    def area_heron(r, s, t):
        a, b, c = math.hypot(r[0] - s[0], r[1] - s[1]), math.hypot(r[0] - t[0], r[1] - t[1]), math.hypot(s[0] - t[0],
                                                                                                         s[1] - t[1])
        s = (a + b + c) / 2
        return (max(0, s * (s - a) * (s - b) * (s - c))) ** .5


def main():
    s = Solution()
    print(s.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 406 ms, faster than 31.31% of Python3 online submissions for Largest Triangle Area.
Memory Usage: 14 MB, less than 27.93% of Python3 online submissions for Largest Triangle Area.

2. Runtime: 527 ms, faster than 24.55% of Python3 online submissions for Largest Triangle Area.
Memory Usage: 13.9 MB, less than 27.93% of Python3 online submissions for Largest Triangle Area.
"""
