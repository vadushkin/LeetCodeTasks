import collections


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        img1_points, img2_points, d = [], [], collections.defaultdict(int)

        for r in range(len(img1)):
            for c in range(len(img1[0])):
                if img1[r][c]:
                    img1_points.append((r, c))

                if img2[r][c]:
                    img2_points.append((r, c))

        for r_a, c_a in img1_points:
            for r_b, c_b in img2_points:
                d[(r_b - r_a, c_b - c_a)] += 1

        return max(d.values() or [0])


def main():
    s = Solution()
    print(s.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 821 ms, faster than 67.84% of Python3 online submissions for Image Overlap.
Memory Usage: 14.7 MB, less than 43.86% of Python3 online submissions for Image Overlap.

2. Runtime: 996 ms, faster than 56.14% of Python3 online submissions for Image Overlap.
Memory Usage: 14.7 MB, less than 43.86% of Python3 online submissions for Image Overlap.
"""
