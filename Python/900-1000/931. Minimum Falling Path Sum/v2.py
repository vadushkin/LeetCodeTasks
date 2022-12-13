from functools import reduce


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        padding = [float('inf')]

        def combine_rows(lower_row, upper_row):
            return [upper + min(lower_left, lower_mid, lower_right)
                    for upper, lower_left, lower_mid, lower_right in
                    zip(upper_row, lower_row[1:] + padding, lower_row, padding + lower_row[:-1])]

        return min(reduce(combine_rows, matrix[::-1]))


def main():
    s = Solution()
    print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 317 ms Beats 52.70%
   Memory 14.6 MB Beats 99.5%

2. Runtime 162 ms Beats 84.35%
   Memory 14.7 MB Beats 91.12%
"""
