from functools import cache
from math import inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, prev, prev_cnt, k):
            if k < 0:
                return inf
            if i == len(s):
                return 0
            delete = dp(i + 1, prev, prev_cnt, k - 1)
            if s[i] == prev:
                keep = dp(i + 1, prev, prev_cnt + 1, k)
                if prev_cnt in [1, 9, 99]:
                    keep += 1
            else:
                keep = dp(i + 1, s[i], 1, k) + 1
            return min(delete, keep)

        return dp(0, "", 0, k)


def main():
    s = Solution()
    print(s.getLengthOfOptimalCompression("llllllllllttttttttt", 1))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 6184 ms, faster than 13.50% of Python3 online submissions for String Compression II.
Memory Usage: 367.2 MB, less than 43.56% of Python3 online submissions for String Compression II.

2. Runtime: 2137 ms, faster than 79.14% of Python3 online submissions for String Compression II.
Memory Usage: 368.2 MB, less than 39.88% of Python3 online submissions for String Compression II.
"""
