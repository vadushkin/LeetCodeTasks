def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)

            if res == 0:
                return mid

            if res == -1:
                high = mid - 1
            else:
                low = mid + 1

        return -1


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 51 ms Beats 62.30%
   Memory 14 MB Beats 16.19%

2. Runtime 60 ms Beats 29.55%
   Memory 14 MB Beats 16.19%
"""
