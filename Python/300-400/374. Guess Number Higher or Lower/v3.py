from bisect import bisect_left


def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n), 0, key=lambda num: -guess(num))


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 36 ms Beats 47.21% 
   Memory 13.9 MB Beats 56.88%

2. Runtime 18 ms Beats 99.87% 
   Memory 13.8 MB Beats 56.88%
"""
