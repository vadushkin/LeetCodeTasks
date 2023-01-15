class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = 1

        while n > a:
            a = a * 2 + 1

        return n ^ a

def main():
    s = Solution()
    print(s.bitwiseComplement(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 33 ms Beats 72.77%
   Memory 13.8 MB Beats 93.35%

2. Runtime 29 ms Beats 86.87% 
   Memory 13.7 MB Beats 93.35% 
"""
