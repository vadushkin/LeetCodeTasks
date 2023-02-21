from itertools import accumulate


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """For fun."""
        record = sorted([[interval[0], 1] for interval in intervals] + [[interval[1], -1] for interval in intervals],
                        key=lambda intervals_value: intervals_value[0] * 10 - intervals_value[1])

        pos_gap = [e_index for e_index, count in enumerate(accumulate([rec[1] for rec in record])) if count == 0]

        return [[record[0][0], record[pos_gap[0]][0]]] + \
            [[record[pos_gap[i] + 1][0], record[pos_gap[i + 1]][0]] for i in range(0, len(pos_gap) - 1)]


def main():
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 176 ms Beats 18.50% 
   Memory 19.3 MB Beats 8.7%

2. Runtime 174 ms Beats 19.13% 
   Memory 19.4 MB Beats 8.7%
"""
