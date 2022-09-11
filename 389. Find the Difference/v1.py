class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


def main():
    s = Solution()
    print(s.findTheDifference("asd", "asdf"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 48.33% of Python3 online submissions for Find the Difference.
Memory Usage: 13.8 MB, less than 76.73% of Python3 online submissions for Find the Difference.

2. Runtime: 72 ms, faster than 20.43% of Python3 online submissions for Find the Difference.
Memory Usage: 14 MB, less than 32.06% of Python3 online submissions for Find the Difference.
"""
