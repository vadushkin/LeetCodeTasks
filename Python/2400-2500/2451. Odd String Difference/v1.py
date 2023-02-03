from collections import defaultdict


class Solution:
    def oddString(self, words: list[str]) -> str:
        odd_strings = defaultdict(list)

        for i in range(len(words)):
            odd_string = ''

            for j in range(len(words[i]) - 1, 0, -1):
                odd_string += str(ord(words[i][j]) - ord(words[i][j - 1])) + "!"

            odd_strings[odd_string].append(words[i])

        for values in odd_strings.values():
            if len(values) == 1:
                return values[0]

        return ""


def main():
    s = Solution()
    print(s.oddString(["abm","bcn","alm"]))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 40 ms Beats 58.1% 
   Memory 13.8 MB Beats 98.84%

2. Runtime 33 ms Beats 87.73% 
   Memory 13.9 MB Beats 71.45%
"""
