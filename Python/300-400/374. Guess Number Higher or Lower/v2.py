def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            if guess(mid) > 0:
                low = mid + 1
            else:
                high = mid - 1

        return low


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 57 ms Beats 42.17%
   Memory 14 MB Beats 16.19%

2. Runtime 47 ms Beats 71.68%
   Memory 13.9 MB Beats 66.34%
"""
