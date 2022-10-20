class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, w_to_p = s.split(' '), dict()

        if len(pattern) != len(words): return False
        if len(set(pattern)) != len(set(words)): return False

        for i in range(len(words)):
            if words[i] not in w_to_p:
                w_to_p[words[i]] = pattern[i]
            elif w_to_p[words[i]] != pattern[i]:
                return False
        return True


def main():
    s = Solution()
    print(s.wordPattern("12321", "hero ero ro ero hero"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 29.17% of Python3 online submissions for Word Pattern.
Memory Usage: 13.6 MB, less than 99.80% of Python3 online submissions for Word Pattern.

2. Runtime: 60 ms, faster than 18.03% of Python3 online submissions for Word Pattern.
Memory Usage: 14 MB, less than 24.20% of Python3 online submissions for Word Pattern.
"""
