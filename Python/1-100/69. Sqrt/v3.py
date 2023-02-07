class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt_x = x + 1

        while sqrt_x * sqrt_x > x:
            sqrt_x = int(sqrt_x - (sqrt_x * sqrt_x - x) / (2 * sqrt_x))

        return sqrt_x


def main():
    s = Solution()
    print(s.mySqrt(4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 45 ms Beats 53.85%
   Memory 13.9 MB Beats 49%

2. Runtime 36 ms Beats 82.32%
   Memory 13.9 MB Beats 8.16%
"""
