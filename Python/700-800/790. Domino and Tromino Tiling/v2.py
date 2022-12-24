class Solution:
    def numTilings(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        match n:
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 5
            case 4:
                return 11
            case 5:
                return 24

        a, b, c = 5, 11, 24

        for i in range(6, n + 1):
            a, b, c = b, c, 2 * c + a

        return c % MOD


def main():
    s = Solution()
    print(s.numTilings(3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 30 ms Beats 97.62%
   Memory 13.8 MB Beats 85.40%
   
2. Runtime 33 ms Beats 95.87%
   Memory 13.9 MB Beats 85.40%
"""
