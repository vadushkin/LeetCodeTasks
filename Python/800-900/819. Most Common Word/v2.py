class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        d, res, count = {}, "", 0

        for word in paragraph.lower().split():
            if word in banned:
                continue

            d[word] = 1 + d.get(word, 0)

            if d[word] > count:
                count = d[word]
                res = word

        return res


def main():
    s = Solution()
    print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 46 ms Beats 63.66% 
   Memory 13.8 MB Beats 80.24%

2. Runtime 37 ms Beats 87.37% 
   Memory 13.9 MB Beats 34.58%
"""
