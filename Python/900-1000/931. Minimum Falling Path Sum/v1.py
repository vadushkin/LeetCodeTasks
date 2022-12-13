class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        for i in range(1, M):
            for j in range(N):
                a = matrix[i - 1][j - 1] if 0 <= j - 1 else float('inf')
                b = matrix[i - 1][j]
                c = matrix[i - 1][j + 1] if j + 1 < N else float('inf')
                matrix[i][j] += min(a, b, c)

        return min(matrix[M - 1])


def main():
    s = Solution()
    print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 308 ms Beats 56.6% 
   Memory 14.9 MB Beats 27.28%
   
2. Runtime 363 ms Beats 34.65%
   Memory 14.9 MB Beats 27.28% 
"""
