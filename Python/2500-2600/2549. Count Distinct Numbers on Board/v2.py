class Solution:
    def distinctIntegers(self, n: int) -> int:
        return max(n - 1, 1)


def main():
    s = Solution()
    print(s.distinctIntegers(5))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 26 ms Beats 93.57% 
   Memory 13.8 MB Beats 91.43%

2. Runtime 32 ms Beats 73.36%
   Memory 13.8 MB Beats 91.43%
"""
