from functools import reduce


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return reduce(lambda s, i: (s << i.bit_length() | i) % 1000000007, range(1, n + 1))


def main():
    s = Solution()
    print(s.concatenatedBinary(3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2570 ms, faster than 54.33% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 13.9 MB, less than 62.20% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.

2. Runtime: 3109 ms, faster than 38.58% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 13.9 MB, less than 80.31% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
"""
