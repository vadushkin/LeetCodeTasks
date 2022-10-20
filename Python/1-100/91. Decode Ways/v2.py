class Solution:
    def numDecodings(self, s: str) -> int:
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w


def main():
    s = Solution()
    print(s.numDecodings("12"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 59 ms, faster than 43.06% of Python3 online submissions for Decode Ways.
Memory Usage: 13.8 MB, less than 80.35% of Python3 online submissions for Decode Ways.

2. Runtime: 70 ms, faster than 16.35% of Python3 online submissions for Decode Ways.
Memory Usage: 13.9 MB, less than 46.16% of Python3 online submissions for Decode Ways.
"""
