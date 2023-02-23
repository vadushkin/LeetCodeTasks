class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '#' + '#'.join(s) + '#'
        res = 0

        for index in range(len(s)):
            length = 0

            while index - length >= 0 and index + length < len(s) and s[index + length] == s[index - length]:
                length += 1

            res += length // 2

        return res


def main():
    s = Solution()
    print(s.countSubstrings("abababa"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 264 ms Beats 32.16% 
   Memory 13.8 MB Beats 97.62%

2. Runtime 257 ms Beats 32.78% 
   Memory 13.7 MB Beats 97.62%
"""
