class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        res = []
        for i in words:
            word_set = set(i.lower())
            if (word_set & set1 == word_set) or (word_set & set2 == word_set) or (word_set & set3 == word_set):
                res.append(i)
        return res


def main():
    s = Solution()
    print(s.findWords(["hello", "my", "friend"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 63.33% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.9 MB, less than 16.84% of Python3 online submissions for Keyboard Row.

2. Runtime: 50 ms, faster than 60.91% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.9 MB, less than 68.26% of Python3 online submissions for Keyboard Row.
"""
