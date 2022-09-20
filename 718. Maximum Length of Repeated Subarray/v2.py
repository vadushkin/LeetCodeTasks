from functools import reduce


class Solution:
    def findLength(self, A: list[int], B: list[int]) -> int:
        return max(map(max,
                       reduce(lambda y, a: y + [[a == b and (1 + (i and y[-1][i - 1])) for i, b in enumerate(B)]], A,
                              [[0] * len(B)])))


def main():
    s = Solution()
    print(s.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1942 ms, faster than 91.97% of Python3 online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 43.7 MB, less than 12.58% of Python3 online submissions for Maximum Length of Repeated Subarray.  

2. Runtime: 5681 ms, faster than 54.28% of Python3 online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 43.8 MB, less than 12.58% of Python3 online submissions for Maximum Length of Repeated Subarray.
"""
