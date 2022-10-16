class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


def main():
    s = Solution()
    print(s.canWinNim(13))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 57 ms, faster than 23.72% of Python3 online submissions for Nim Game.
Memory Usage: 13.8 MB, less than 93.58% of Python3 online submissions for Nim Game.

2. Runtime: 45 ms, faster than 58.45% of Python3 online submissions for Nim Game.
Memory Usage: 13.8 MB, less than 93.58% of Python3 online submissions for Nim Game.
"""
