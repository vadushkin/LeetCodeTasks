class Solution:
    def removeDuplicates(self, s: str) -> str:

        i = 0

        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                if i > 0:
                    i -= 1
            else:
                i += 1

        return s


def main():
    s = Solution()
    print(s.removeDuplicates("aaaaaaaa"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1292 ms Beats 5.2%
   Memory 14.7 MB Beats 97.75%

2. Runtime 1400 ms Beats 5.2%
   Memory 14.7 MB Beats 86.70%
"""
