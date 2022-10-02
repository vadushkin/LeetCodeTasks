class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(q) for q in letters if s.count(q) == 1]
        return min(index) if len(index) > 0 else -1


def main():
    s = Solution()
    print(s.firstUniqChar("leetcode"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 99.09% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.1 MB, less than 95.19% of Python3 online submissions for First Unique Character in a String.

2. Runtime: 89 ms, faster than 93.78% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14 MB, less than 95.19% of Python3 online submissions for First Unique Character in a String.
"""
