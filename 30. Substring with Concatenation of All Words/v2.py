from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        wlen = len(words[0])
        wslen = len(words) * len(words[0])
        res = []

        for pos in range(wlen):
            i = pos
            d = Counter(words)

            for j in range(i, len(s) + 1 - wlen, wlen):
                word = s[j: j + wlen]
                d[word] -= 1

                while d[word] < 0:
                    d[s[i: i + wlen]] += 1
                    i += wlen
                if i + wslen == j + wlen:
                    res.append(i)

        return res


def main():
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 262 ms, faster than 62.19% of Python3 online submissions for Substring with Concatenation of All Words.
Memory Usage: 14.1 MB, less than 97.94% of Python3 online submissions for Substring with Concatenation of All Words.

2. Runtime: 191 ms, faster than 66.03% of Python3 online submissions for Substring with Concatenation of All Words.
Memory Usage: 14.3 MB, less than 33.67% of Python3 online submissions for Substring with Concatenation of All Words.
"""
