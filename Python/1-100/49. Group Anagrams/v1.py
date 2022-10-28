from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = defaultdict(list)

        for word in strs:
            seen[''.join(sorted(word))].append(word)

        return [list_items for list_items in seen.values()]


def main():
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 225 ms, faster than 46.54% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.2 MB, less than 88.69% of Python3 online submissions for Group Anagrams.

2. Runtime: 267 ms, faster than 22.28% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.2 MB, less than 80.07% of Python3 online submissions for Group Anagrams.
"""
