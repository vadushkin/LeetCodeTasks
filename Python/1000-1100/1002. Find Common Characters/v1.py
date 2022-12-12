from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if not words:
            return []

        x = Counter(words[0])

        for items in words[1:]:
            x &= Counter(items)

        return list(x.elements())


def main():
    s = Solution()
    print(s.commonChars(['banana', 'among', 'us']))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 73 ms Beats 76.7%
   Memory 13.9 MB Beats 94.94%

2. Runtime 42 ms Beats 98.94%
   Memory 14 MB Beats 65.94%
"""
