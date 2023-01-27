class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        res = []
        pre_words = set()

        words.sort(key=len)

        for word in words:
            if self.word_break(word, pre_words):
                res.append(word)

            pre_words.add(word)

        return res

    @staticmethod
    def word_break(string: str, words: set[str]) -> list[bool] | bool:
        if not words:
            return False

        dp = [False] * (len(string) + 1)
        dp[0] = True

        for i in range(len(string) + 1):
            for j in range(i):
                if dp[j] and string[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]


def main():
    s = Solution()
    print(s.findAllConcatenatedWordsInADict(
        ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 2030 ms Beats 10.81% 
   Memory 17.5 MB Beats 72.49%

2. Runtime 660 ms Beats 44.72% 
   Memory 16.6 MB Beats 90.74%
"""
