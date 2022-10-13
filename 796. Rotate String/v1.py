class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in s:
            goal = goal[1:] + goal[0]
            if s == goal:
                return True
        return False


def main():
    s = Solution()
    print(s.rotateString("abcde", "cdeab"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 67 ms, faster than 12.15% of Python3 online submissions for Rotate String.
Memory Usage: 14 MB, less than 13.03% of Python3 online submissions for Rotate String.

2. Runtime: 65 ms, faster than 15.34% of Python3 online submissions for Rotate String.
Memory Usage: 14 MB, less than 13.03% of Python3 online submissions for Rotate String.
"""
