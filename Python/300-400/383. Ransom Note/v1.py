class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not (1 <= len(ransomNote) <= 100000) or not (1 <= len(magazine) <= 100000):
            return False
        ransomNote, magazine = sorted(ransomNote), sorted(magazine)
        i = 0
        while ransomNote and i != len(magazine):
            if ransomNote[0] != magazine[i]:
                i += 1
                continue
            ransomNote.pop(0)
            i += 1
        if ransomNote:
            return False
        return True


def main():
    s = Solution()
    print(s.canConstruct('abbdddddddddde', 'bbddddddddddaaa'))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 133 ms, faster than 20.84% of Python3 online submissions for Ransom Note.
Memory Usage: 14.4 MB, less than 12.37% of Python3 online submissions for Ransom Note.

2. Runtime: 228 ms, faster than 5.30% of Python3 online submissions for Ransom Note.
Memory Usage: 14.3 MB, less than 20.43% of Python3 online submissions for Ransom Note.
"""
