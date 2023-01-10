class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        return sum(''.join(r).replace('.', '').count('Rp') for r in board + list(zip(*board)) for r in [r, r[::-1]])


def main():
    s = Solution()
    print(s.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", "p", ".", ".", ".", "."],
                             [".", ".", ".", "R", ".", ".", ".", "p"],
                             [".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", "p", ".", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", "."],
                             [".", ".", ".", ".", ".", ".", ".", "."]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 36 ms Beats 74.86%
   Memory 13.8 MB Beats 98.84%

2. Runtime 33 ms Beats 83.24% 
   Memory 13.9 MB Beats 83.81%
"""
