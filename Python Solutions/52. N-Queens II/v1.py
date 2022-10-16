class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, xy_dif, xy_sum):
            len_que = len(queens)
            if len_que == n:
                result.append(queens)
                return None
            for queen in range(n):
                if queen not in queens and len_que - queen not in xy_dif and len_que + queen not in xy_sum:
                    dfs(queens + [queen], xy_dif + [len_que - queen], xy_sum + [len_que + queen])

        result = []
        dfs([], [], [])
        return len(result)


def main():
    s = Solution()
    print(s.totalNQueens(4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 71 ms, faster than 74.54% of Python3 online submissions for N-Queens II.
Memory Usage: 14 MB, less than 37.18% of Python3 online submissions for N-Queens II.

2. Runtime: 85 ms, faster than 59.44% of Python3 online submissions for N-Queens II.
Memory Usage: 13.9 MB, less than 37.18% of Python3 online submissions for N-Queens II.
"""
