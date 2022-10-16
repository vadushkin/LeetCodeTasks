class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = 9 * e0 + 9 * e1 + 6 * e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0


def main():
    s = Solution()
    print(s.numDecodings("1*"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 277 ms, faster than 97.84% of Python3 online submissions for Decode Ways II.
Memory Usage: 14.9 MB, less than 98.92% of Python3 online submissions for Decode Ways II.

2. Runtime: 985 ms, faster than 54.68% of Python3 online submissions for Decode Ways II.
Memory Usage: 15 MB, less than 79.86% of Python3 online submissions for Decode Ways II.
"""
