from functools import lru_cache


class Solution:
    @lru_cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        for i in range(1, len(s1)):
            l1, r1 = sorted(s1[:i]), sorted(s1[i:])

            if l1 == sorted(s2[:i]) and r1 == sorted(s2[i:]):
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                    return True

            if l1 == sorted(s2[-i:]) and r1 == sorted(s2[:-i]):
                if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                    return True

        return False


def main():
    s = Solution()
    print(s.isScramble("great", "rgeat"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 48 ms Beats 83.33% 
   Memory 14 MB Beats 89.4%

2. Runtime 47 ms Beats 84.72% 
   Memory 13.8 MB Beats 99.7%
"""
