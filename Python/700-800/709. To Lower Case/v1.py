class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


def main():
    s = Solution()
    print(s.toLowerCase("HELLO WORLD!!!!!!"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 50 ms Beats 66.30%
   Memory 13.9 MB Beats 51.74%

2. Runtime 28 ms Beats 97.57%
   Memory 13.8 MB Beats 51.74% 
"""
