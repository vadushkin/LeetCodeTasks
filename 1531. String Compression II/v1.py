from functools import lru_cache
from math import inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def counts(k, i, j, c):

            if k < 0:
                return inf

            if i >= n:
                return 0

            if 0 <= j < n and s[i] == s[j]:
                return int(c == 1 or c == 9 or c == 99) + counts(k, i + 1, i, c + 1)

            return min(1 + counts(k, i + 1, i, 1), counts(k - 1, i + 1, j, c))

        return counts(k, 0, -1, 0)


def main():
    s = Solution()
    print(s.getLengthOfOptimalCompression("aaaaa", 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4687 ms, faster than 33.74% of Python3 online submissions for String Compression II.
Memory Usage: 365.2 MB, less than 45.40% of Python3 online submissions for String Compression II.

2. Runtime: 2070 ms, faster than 82.82% of Python3 online submissions for String Compression II.
Memory Usage: 367.7 MB, less than 42.94% of Python3 online submissions for String Compression II.
"""
