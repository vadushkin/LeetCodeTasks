class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pascal = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal[rowIndex]


def main():
    s = Solution()
    print(s.getRow(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 57 ms, faster than 26.96% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 63.27% of Python3 online submissions for Pascal's Triangle II.

2. Runtime: 43 ms, faster than 66.96% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.9 MB, less than 63.27% of Python3 online submissions for Pascal's Triangle II.
"""
