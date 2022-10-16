class Solution:
    def isAnagram(self, s, t):
        dic1, dic2 = [0] * 26, [0] * 26
        for item in s:
            dic1[ord(item) - ord('a')] += 1
        for item in t:
            dic2[ord(item) - ord('a')] += 1
        return dic1 == dic2


def main():
    s = Solution()
    print(s.isAnagram("asd", "dsa"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 90 ms, faster than 32.12% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 67.20% of Python3 online submissions for Valid Anagram.

2. Runtime: 53 ms, faster than 88.29% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 97.11% of Python3 online submissions for Valid Anagram.
"""
