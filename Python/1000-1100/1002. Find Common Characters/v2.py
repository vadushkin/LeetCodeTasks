class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if len(words) <= 1:
            return words

        res = []
        all_char = set(words[0])

        for char in all_char:
            min_freq = min(word.count(char) for word in words)

            if min_freq:
                res += [char] * min_freq

        return res


def main():
    s = Solution()
    print(s.commonChars(["cool", "lock", "cook"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 73 ms Beats 76.7%
   Memory 14.1 MB Beats 28.66%

2. Runtime 99 ms Beats 54.9%
   Memory 13.9 MB Beats 65.94%
"""
