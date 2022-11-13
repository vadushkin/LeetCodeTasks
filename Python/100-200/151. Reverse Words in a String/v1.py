class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


def main():
    s = Solution()
    print(s.reverseWords(" a good example"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 66 ms Beats 39.98%
   Memory 13.8 MB Beats 97.78%

2. Runtime 52 ms Beats 73.5% 
   Memory 14 MB Beats 48.44%
"""
