class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


def main():
    s = Solution()
    print(s.isAnagram("amognus", "amongus"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 63 ms, faster than 72.79% of Python3 online submissions for Valid Anagram.
Memory Usage: 15.2 MB, less than 11.94% of Python3 online submissions for Valid Anagram.

2. Runtime: 91 ms, faster than 30.67% of Python3 online submissions for Valid Anagram.
Memory Usage: 15 MB, less than 21.80% of Python3 online submissions for Valid Anagram.
"""
