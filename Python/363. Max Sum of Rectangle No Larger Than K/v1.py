from bisect import bisect_right, insort
from math import inf


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = -inf
        for d in range(n):
            rowSums = [0] * m
            for r in range(d, n):
                for i in range(m):
                    rowSums[i] += matrix[i][r]
                colSums = [0]
                colSum = 0
                for rowSum in rowSums:
                    colSum += rowSum
                    diff = colSum - k
                    idx = bisect_right(colSums, diff)
                    if idx - 1 >= 0 and colSums[idx - 1] == diff:
                        return k
                    elif idx != len(colSums):
                        res = max(res, colSum - colSums[idx])
                    insort(colSums, colSum)
        return res


def main():
    s = Solution()
    print(s.maxSumSubmatrix([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 100))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2896 ms, faster than 79.44% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
Memory Usage: 14.7 MB, less than 74.31% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.

2. Runtime: 2552 ms, faster than 84.98% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
Memory Usage: 14.7 MB, less than 92.49% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
"""
