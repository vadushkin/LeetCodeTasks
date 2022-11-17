class Solution:
    def computeArea(self,
                    ax1: int, ay1: int,
                    ax2: int, ay2: int,
                    bx1: int, by1: int,
                    bx2: int, by2: int
                    ) -> int:
        overlap_x = overlap_y = 0

        if min(ax2, bx2) > max(ax1, bx1):
            overlap_x = min(ax2, bx2) - max(ax1, bx1)
        if min(ay2, by2) > max(ay1, by1):
            overlap_y = min(ay2, by2) - max(ay1, by1)

        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * \
               (by2 - by1) - overlap_x * overlap_y


def main():
    s = Solution()
    print(s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 125 ms Beats 18.99%
   Memory 14 MB Beats 71.27%

2. Runtime 126 ms Beats 17.88%
   Memory 14 MB Beats 71.27%
"""
