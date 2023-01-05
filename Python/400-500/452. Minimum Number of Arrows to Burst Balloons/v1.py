class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        res, cur_start = 1, points[-1][0]

        for start, end in reversed(points):
            if end < cur_start:
                cur_start = start
                res += 1

        return res


def main():
    s = Solution()
    print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 3204 ms Beats 33.42%
   Memory 59.8 MB Beats 70.29%
 
2. Runtime 1398 ms Beats 76.81%
   Memory 59.9 MB Beats 35.51%
"""
