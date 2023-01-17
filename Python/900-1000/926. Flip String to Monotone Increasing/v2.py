class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num = 0

        for c in s:
            if c == '0':
                ans = min(num, ans + 1)
            else:
                num += 1

        return ans


def main():
    s = Solution()
    print(s.minFlipsMonoIncr("00110"))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 143 ms Beats 91.35%
   Memory 15 MB Beats 72.76%

2. Runtime 141 ms Beats 92.31%
   Memory 14.9 MB Beats 72.76%
"""
