class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = 1

        while n > a:
            a = a * 2 + 1

        return a - n


def main():
    s = Solution()
    print(s.bitwiseComplement(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 37 ms Beats 54.94%
   Memory 13.8 MB Beats 93.35%

2. Runtime 42 ms Beats 41.33% 
   Memory 13.8 MB Beats 93.35%
"""
