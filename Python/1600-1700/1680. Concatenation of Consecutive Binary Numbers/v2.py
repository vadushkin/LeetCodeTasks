class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = 0
        for i in range(1, n + 1):
            s = (s << i.bit_length() | i) % 1000000007
        return s


def main():
    s = Solution()
    print(s.concatenatedBinary(10))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1307 ms, faster than 93.70% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 13.9 MB, less than 80.31% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.

2. Runtime: 3110 ms, faster than 38.58% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 13.8 MB, less than 97.64% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
"""
