import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        return collections.Counter(word for word in re.findall(r'\w+', paragraph.lower())
                                   if word not in set(banned)).most_common(1)[0][0]


def main():
    s = Solution()
    print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 42 ms Beats 73.75% 
   Memory 13.8 MB Beats 80.24%

2. Runtime 36 ms Beats 89.56%
   Memory 13.9 MB Beats 34.58%
"""
