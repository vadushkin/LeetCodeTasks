class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = 0
        bit = 1 << 15

        while bit > 0:
            root |= bit

            if root > num // root:
                root ^= bit

            bit >>= 1

        return root * root == num


def main():
    s = Solution()
    print(s.isPerfectSquare(16))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 31 ms Beats 77.45% 
   Memory 13.7 MB Beats 94.91%

2. Runtime 34 ms Beats 62.50% 
   Memory 13.9 MB Beats 47.29%
"""
