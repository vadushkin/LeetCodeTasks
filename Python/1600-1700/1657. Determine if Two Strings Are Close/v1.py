import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)

        set1 = set(word1)
        set2 = set(word2)

        s1 = sorted(c1.values())
        s2 = sorted(c2.values())

        return s1 == s2 and set1 == set2


def main():
    s = Solution()
    print(s.closeStrings("aaab", "bbba"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 338 ms Beats 61.60% 
   Memory 15.5 MB Beats 16.80%

2. Runtime 165 ms Beats 89.20%
   Memory 15.3 MB Beats 43.60%
"""
