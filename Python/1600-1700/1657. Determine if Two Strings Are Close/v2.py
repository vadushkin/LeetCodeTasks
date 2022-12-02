class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        w1 = []
        w2 = []

        for i in set(word1):
            w1.append(word1.count(i))
            w2.append(word2.count(i))

        if sorted(w1) == sorted(w2):
            return True
        return False


def main():
    s = Solution()
    print(s.closeStrings("abs", "sba"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 167 ms Beats 89.20%
   Memory 15.4 MB Beats 16.80%

2. Runtime 175 ms Beats 87.20%
   Memory 15.4 MB Beats 16.80%
"""
