"""
class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j: continue
                if words[i] + words[j] == str(words[i] + words[j])[::-1]:
                    ans.append([i, j])
        return ans


# 84 / 136 test cases passed.
# Status: Time Limit Exceeded
"""

"""
class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        ans = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if i == j: continue
                if words[i] + words[j] == str(words[i] + words[j])[::-1]:
                    ans.append([i, j])
                if words[j] + words[i] == str(words[j] + words[i])[::-1]:
                    ans.append([j, i])
        return ans

# 106 / 136 test cases passed.
# Status: Time Limit Exceeded
"""


class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        lookup = {w: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                pre, pos = w[:j], w[j:]
                if pre == pre[::-1] and pos[::-1] != w and pos[::-1] in lookup:
                    res.append([lookup[pos[::-1]], i])
                if j != len(w) and pos == pos[::-1] and pre[::-1] != w and pre[::-1] in lookup:
                    res.append([i, lookup[pre[::-1]]])
        return res


def main():
    s = Solution()
    print(s.palindromePairs(["d", "gr", "dd", "rg"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 7635 ms, faster than 14.64% of Python3 online submissions for Palindrome Pairs.
Memory Usage: 26.4 MB, less than 85.90% of Python3 online submissions for Palindrome Pairs.

2. Runtime: 8212 ms, faster than 8.00% of Python3 online submissions for Palindrome Pairs.
Memory Usage: 26.4 MB, less than 85.90% of Python3 online submissions for Palindrome Pairs.
"""
