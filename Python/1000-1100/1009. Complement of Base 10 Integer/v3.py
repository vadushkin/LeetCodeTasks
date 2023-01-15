class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return (1 << len(bin(n)) >> 2) - n - 1


def main():
    s = Solution()
    print(s.bitwiseComplement(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 29 ms Beats 86.87%
   Memory 13.8 MB Beats 93.35%
 
2. Runtime 19 ms Beats 99.84%
   Memory 13.7 MB Beats 93.35%
"""
