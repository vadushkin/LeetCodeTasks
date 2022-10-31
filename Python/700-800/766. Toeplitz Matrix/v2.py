class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))


def main():
    s = Solution()
    print(s.isToeplitzMatrix())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 202 ms, faster than 34.61% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 13.9 MB, less than 36.74% of Python3 online submissions for Toeplitz Matrix.

2. Runtime: 90 ms, faster than 93.67% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 13.8 MB, less than 78.65% of Python3 online submissions for Toeplitz Matrix.
"""
