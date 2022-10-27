from scipy.signal import convolve2d


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        img1 = [row[::-1] for row in img1][::-1]
        res = convolve2d(img2, img1)
        return res.max()


def main():
    s = Solution()
    print(s.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1006 ms, faster than 54.97% of Python3 online submissions for Image Overlap.
Memory Usage: 75.2 MB, less than 5.26% of Python3 online submissions for Image Overlap.

2. Runtime: 899 ms, faster than 63.16% of Python3 online submissions for Image Overlap.
Memory Usage: 74.6 MB, less than 5.26% of Python3 online submissions for Image Overlap.
"""
