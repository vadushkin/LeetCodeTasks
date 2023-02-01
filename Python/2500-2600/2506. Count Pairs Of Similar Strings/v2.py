class Solution:
    def similarPairs(self, words: list[str]) -> int:
        return sum(set(x) == set(y) for i, x in enumerate(words) for y in words[i + 1:])


def main():
    s = Solution()
    print(s.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 467 ms Beats 30.42%
   Memory 13.8 MB Beats 96.42%

2. Runtime 434 ms Beats 35.83%
   Memory 14 MB Beats 70.32%
"""
