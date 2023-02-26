from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return j

            if j == 0:
                return i

            if word1[i - 1] == word2[j - 1]:
                return dp(i - 1, j - 1)

            return min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1

        return dp(len(word1), len(word2))


def main():
    s = Solution()
    print(s.minDistance("horse", "ros"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 74 ms Beats 99.3% 
   Memory 17 MB Beats 75.33%

2. Runtime 70 ms Beats 99.49% 
   Memory 17 MB Beats 73.36%
"""
