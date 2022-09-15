class Solution:
    def canWinNim(self, n: int) -> bool:
        return n & 3


def main():
    s = Solution()
    print(s.canWinNim(3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 20.84% of Python3 online submissions for Nim Game.
Memory Usage: 13.9 MB, less than 45.91% of Python3 online submissions for Nim Game.

2. Runtime: 29 ms, faster than 95.78% of Python3 online submissions for Nim Game.
Memory Usage: 13.8 MB, less than 93.58% of Python3 online submissions for Nim Game.
"""
