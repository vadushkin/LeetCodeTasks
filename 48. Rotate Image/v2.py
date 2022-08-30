class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def main():
    s = Solution()
    print(s.rotate([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
                   ))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 54 ms, faster than 54.37% of Python3 online submissions for Rotate Image.
Memory Usage: 14 MB, less than 29.99% of Python3 online submissions for Rotate Image.

2. Runtime: 66 ms, faster than 24.76% of Python3 online submissions for Rotate Image.
Memory Usage: 13.8 MB, less than 98.34% of Python3 online submissions for Rotate Image.
"""
