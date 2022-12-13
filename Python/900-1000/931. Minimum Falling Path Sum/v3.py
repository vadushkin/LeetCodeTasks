from functools import reduce


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        return min(reduce(lambda lower_row, upper_row: [upper + min(lower_left, lower_mid, lower_right)
                                                        for upper, lower_left, lower_mid, lower_right
                                                        in zip(upper_row, lower_row[1:] + [float('inf')], lower_row,
                                                               [float('inf')] + lower_row[:-1])], matrix[::-1]))


def main():
    s = Solution()
    print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 276 ms Beats 64.79%
   Memory 14.7 MB Beats 64.34%

2. Runtime 310 ms Beats 55.21%
Memory 14.6 MB Beats 91.12%
"""
