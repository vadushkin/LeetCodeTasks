class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal


def main():
    s = Solution()
    print(s.generate(3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 43 ms, faster than 64.27% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14 MB, less than 17.81% of Python3 online submissions for Pascal's Triangle.

2. Runtime: 47 ms, faster than 52.98% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 17.81% of Python3 online submissions for Pascal's Triangle.
"""
