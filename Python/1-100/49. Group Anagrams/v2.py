from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        letters_to_words = defaultdict(list)

        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)

        return list(letters_to_words.values())


def main():
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 152 ms, faster than 75.86% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.1 MB, less than 50.70% of Python3 online submissions for Group Anagrams.

2. Runtime: 226 ms, faster than 45.94% of Python3 online submissions for Group Anagrams.
Memory Usage: 18 MB, less than 53.67% of Python3 online submissions for Group Anagrams.
"""
