import collections


class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        diff, rows, cols = collections.defaultdict(list), len(mat), len(mat[0])
        for i in range(rows):
            for j in range(cols):
                diff[i - j].append(mat[i][j])
        for k in diff:
            diff[k].sort()
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = diff[i - j].pop(0)
        return mat


def main():
    s = Solution()
    print(s.diagonalSort([[3, 9],
                          [2, 4],
                          [1, 2],
                          [9, 8],
                          [7, 3]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 86 ms, faster than 93.82% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 14.3 MB, less than 51.34% of Python3 online submissions for Sort the Matrix Diagonally.

2. Runtime: 172 ms, faster than 19.60% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 14.3 MB, less than 51.34% of Python3 online submissions for Sort the Matrix Diagonally.
"""
