class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(bin(n)[2:].translate(''.maketrans('01', '10')), 2)


def main():
    s = Solution()
    print(s.bitwiseComplement(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 34 ms Beats 68.88%
   Memory 13.9 MB Beats 47.65%

2. Runtime 34 ms Beats 68.88% 
   Memory 13.8 MB Beats 93.35%
"""
