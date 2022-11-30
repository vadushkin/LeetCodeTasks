class Solution:
    def trailingZeroes(self, n: int) -> int:
        sm = 0

        for i in range(1, 8):
            sm += n // (5 ** i)

        return sm


def main():
    s = Solution()
    print(s.trailingZeroes(6))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 35 ms Beats 92.79%
   Memory 13.9 MB Beats 22.9%

2. Runtime 63 ms Beats 55.63%
   Memory 13.7 MB Beats 99.80%
"""
