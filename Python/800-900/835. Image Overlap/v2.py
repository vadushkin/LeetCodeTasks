import collections


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)

        pts1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        pts2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        counter = collections.Counter((x1 - x2, y1 - y2) for x1, y1 in pts1 for x2, y2 in pts2)

        return max(counter.values() or [0])


def main():
    s = Solution()
    print(s.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 352 ms, faster than 97.08% of Python3 online submissions for Image Overlap.
Memory Usage: 14.7 MB, less than 43.86% of Python3 online submissions for Image Overlap.

2. Runtime: 1060 ms, faster than 52.05% of Python3 online submissions for Image Overlap.
Memory Usage: 14.8 MB, less than 26.32% of Python3 online submissions for Image Overlap.
"""
