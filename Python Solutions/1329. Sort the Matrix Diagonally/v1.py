class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        #  height matrix [1,2,3] ^
        #                [2,3,4] | - height or len([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
        #                [3,4,5] |
        height = len(mat)
        #  width matrix  [1,2,3]
        #                [2,3,4]
        #                [3,4,5]
        #                ------> - width
        width = len(mat[0])

        # if width == 1 -> this matrix is [[1], [2], [3] etc]
        # just return mat.
        if width == 1:
            return mat

        # this\'s a copy of mat, but it\'s empty.
        matrix = [[[] for _ in range(width)] for _ in range(height)]

        # 2 lists: for example [1,2,3]
        #                      [2,3,4]
        #                      [3,4,5],
        # first = [[], [], []]
        # second = [[], []]
        first = [[] for _ in range(width)]
        second = [[] for _ in range(height - 1)]  # -1, because we take the matrix from the first element matrix[1][0]

        # loop for second list this is [@1, @2, @3]
        #                              [ 2, @3, @4]
        #                              [ 3,  4, @5]
        for i in range(width):
            first[i].append(mat[0][i])
            for j in range(1, height):
                # if index abroad matrix
                if i + j >= width:
                    break
                first[i].append(mat[j][j + i])

        # loop for second list this is [ 1,  2, 3]
        #                              [@2,  3, 4]
        #                              [@3, @4, 5]
        for k in range(1, height):
            second[k - 1].append(mat[k][0])
            for m in range(1, width):
                # if index abroad matrix
                if k + m >= height:
                    break
                second[k - 1].append(mat[m + k][m])

        # sort all lists in the matrix
        sorted_first = [sorted(q) for q in first]
        sorted_second = [sorted(q) for q in second]

        # filling in the matrix on the right
        for e, a in enumerate(sorted_first):
            for e2, b in enumerate(a):
                matrix[e2][e + e2] = b

        # filling in the matrix on the left
        for e3, f in enumerate(sorted_second, start=1):
            for e4, g in enumerate(f):
                matrix[e3 + e4][e4] = g

        return matrix


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
1. Runtime: 107 ms, faster than 76.31% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 15 MB, less than 6.07% of Python3 online submissions for Sort the Matrix Diagonally.

2. Runtime: 132 ms, faster than 55.66% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 15 MB, less than 6.07% of Python3 online submissions for Sort the Matrix Diagonally.
"""
