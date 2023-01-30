class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 1, 0, 0

        for _ in range(n):
            a, b, c = b, c, a + b + c

        return c


def main():
    s = Solution()
    print(s.tribonacci(4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 22 ms Beats 98.52% 
   Memory 13.8 MB Beats 54.1%

2. Runtime 38 ms Beats 41.59% 
   Memory 13.9 MB Beats 54.1%
"""
