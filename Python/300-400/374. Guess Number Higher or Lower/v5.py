import bisect


def guess(num: int) -> int:
    pass


class Solution:
    def __getitem__(self, number: int) -> int:
        return -guess(number)

    def guessNumber(self, n: int) -> int:
        return bisect.bisect_left(self, 0, hi=n)


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 30 ms Beats 79.42% 
   Memory 13.9 MB Beats 9.62%
   
2. Runtime 25 ms Beats 94.57% 
   Memory 13.9 MB Beats 56.88%
"""
