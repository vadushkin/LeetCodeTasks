import string


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not (1 <= len(ransomNote) <= 100000) or not (1 <= len(magazine) <= 100000):
            return False
        return all(ransomNote.count(c) <= magazine.count(c) for c in string.ascii_lowercase)


def main():
    s = Solution()
    print(s.canConstruct('abbdddddddddde', 'bbddddddddddaaa'))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 68 ms, faster than 79.77% of Python3 online submissions for Ransom Note.
Memory Usage: 14.3 MB, less than 20.43% of Python3 online submissions for Ransom Note.

2. Runtime: 73 ms, faster than 73.69% of Python3 online submissions for Ransom Note.
Memory Usage: 14.1 MB, less than 53.79% of Python3 online submissions for Ransom Note.
"""
