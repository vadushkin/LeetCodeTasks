class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n != 1 else 1


def main():
    s = Solution()
    print(s.distinctIntegers(5))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 36 ms Beats 54.98%
   Memory 13.8 MB Beats 43.15%

2. Runtime 32 ms Beats 73.36%
   Memory 14 MB Beats 8.61%
"""
