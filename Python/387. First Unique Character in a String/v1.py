class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] + s[i + 1:]:
                return i
        return -1


def main():
    s = Solution()
    print(s.firstUniqChar("leelcocor"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2966 ms, faster than 8.06% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 16.59% of Python3 online submissions for First Unique Character in a String.

2. Runtime: 452 ms, faster than 14.14% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 16.59% of Python3 online submissions for First Unique Character in a String.
"""
