from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        return sum(not Counter(w) - Counter(chars) and len(w) for w in words)


def main():
    s = Solution()
    print(s.countCharacters(["cat", "bt", "hat", "tree"], "atach"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 389 ms Beats 10.44% 
   Memory 14.4 MB Beats 99.20%

2. Runtime 372 ms Beats 11.15% 
   Memory 14.5 MB Beats 75.13%
"""
