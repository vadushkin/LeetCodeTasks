class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i


def main():
    s = Solution()
    print(s.findTheDifference("asd", "asdf"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 51 ms, faster than 63.93% of Python3 online submissions for Find the Difference.
Memory Usage: 13.7 MB, less than 98.48% of Python3 online submissions for Find the Difference.

2. Runtime: 60 ms, faster than 43.90% of Python3 online submissions for Find the Difference.
Memory Usage: 13.8 MB, less than 98.48% of Python3 online submissions for Find the Difference.
"""
