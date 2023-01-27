class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        d = set(words)

        def dfs(_word: str) -> bool:
            for i in range(1, len(_word)):
                prefix = _word[:i]
                suffix = _word[i:]

                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True

            return False

        res = []

        for word in words:
            if dfs(word):
                res.append(word)

        return res


def main():
    s = Solution()
    print(s.findAllConcatenatedWordsInADict(
        ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 888 ms Beats 34.28%
   Memory 27.6 MB Beats 47.98%

2. Runtime 1158 ms Beats 22.81%
   Memory 27.8 MB Beats 37.94%
"""
