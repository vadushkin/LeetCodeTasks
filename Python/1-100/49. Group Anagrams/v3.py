import itertools


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]


def main():
    s = Solution()
    print(s.groupAnagrams(["bat", "eat", "tea", "can", "anc", "stream"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 279 ms, faster than 18.43% of Python3 online submissions for Group Anagrams.
Memory Usage: 17 MB, less than 96.53% of Python3 online submissions for Group Anagrams.

2. Runtime: 244 ms, faster than 34.78% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.2 MB, less than 80.07% of Python3 online submissions for Group Anagrams.
"""
