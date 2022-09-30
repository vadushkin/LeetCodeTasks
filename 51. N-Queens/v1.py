class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def dfs(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    dfs(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        dfs([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


def main():
    s = Solution()
    print(s.solveNQueens(4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 82 ms, faster than 78.13% of Python3 online submissions for N-Queens.
Memory Usage: 14.6 MB, less than 14.75% of Python3 online submissions for N-Queens.

2. Runtime: 51 ms, faster than 97.96% of Python3 online submissions for N-Queens.
Memory Usage: 14.4 MB, less than 47.24% of Python3 online submissions for N-Queens.
"""
