class Solution(object):
    def __init__(self):
        self.mp = {}

    def isScramble(self, s1, s2):
        n = len(s1)

        if len(s2) != n:
            return False

        if s1 == s2:
            return True

        if n == 1:
            return False

        key = s1 + " " + s2

        if key in self.mp:
            return self.mp[key]

        for i in range(1, n):
            without_swap = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])

            if without_swap:
                return True

            with_swap = self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(s1[i:], s2[:n - i])

            if with_swap:
                return True

        self.mp[key] = False

        return False


def main():
    s = Solution()
    print(s.isScramble("great", "rgeat"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 258 ms Beats 15.74% 
   Memory 14.5 MB Beats 45.99%

2. Runtime 256 ms Beats 16.5% 
   Memory 14.5 MB Beats 49.85%
"""
