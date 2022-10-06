class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        prev_words = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if i != 0 and s[i - 1] != ' ':
                    prev_words += 1
            if prev_words == k:
                return s[0:i]
        return s


def main():
    s = Solution()
    print(s.truncateSentence("Where are you?", 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 61 ms, faster than 24.38% of Python3 online submissions for Truncate Sentence.
Memory Usage: 13.8 MB, less than 61.97% of Python3 online submissions for Truncate Sentence.

2. Runtime: 56 ms, faster than 41.12% of Python3 online submissions for Truncate Sentence.
Memory Usage: 14 MB, less than 15.98% of Python3 online submissions for Truncate Sentence.
"""
