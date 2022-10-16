class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


def main():
    s = Solution()
    print(s.truncateSentence("Hello how are you Contestant", 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 68 ms, faster than 8.94% of Python3 online submissions for Truncate Sentence.
Memory Usage: 13.8 MB, less than 61.97% of Python3 online submissions for Truncate Sentence.

2. Runtime: 51 ms, faster than 56.18% of Python3 online submissions for Truncate Sentence.
Memory Usage: 13.8 MB, less than 96.86% of Python3 online submissions for Truncate Sentence.
"""
