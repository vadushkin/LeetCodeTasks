class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return len([v for v in s[:len(s) // 2] if v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]) == len(
            [v for v in s[len(s) // 2:] if v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']])


def main():
    s = Solution()
    print(s.halvesAreAlike("AbCdEfGh"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 62 ms Beats 61.72%
   Memory 13.9 MB Beats 77.72%

2. Runtime 74 ms Beats 36.61% 
   Memory 14.1 MB Beats 5.13%
"""
