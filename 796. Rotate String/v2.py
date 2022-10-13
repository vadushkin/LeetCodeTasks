class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


def main():
    s = Solution()
    print(s.rotateString("abs", "bsa"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 63.90% of Python3 online submissions for Rotate String.
Memory Usage: 14 MB, less than 13.03% of Python3 online submissions for Rotate String.

2. Runtime: 47 ms, faster than 68.01% of Python3 online submissions for Rotate String.
Memory Usage: 13.7 MB, less than 96.80% of Python3 online submissions for Rotate String.
"""
