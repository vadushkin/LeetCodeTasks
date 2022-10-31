class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        groups = {}

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):

                if r - c not in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False

        return True


def main():
    s = Solution()
    print(s.isToeplitzMatrix([
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 209 ms, faster than 27.56% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 14 MB, less than 6.96% of Python3 online submissions for Toeplitz Matrix.

2. Runtime: 208 ms, faster than 28.48% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 13.9 MB, less than 78.65% of Python3 online submissions for Toeplitz Matrix.
"""
