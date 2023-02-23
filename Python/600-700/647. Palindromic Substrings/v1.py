class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res


def main():
    s = Solution()
    print(s.countSubstrings("abc"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 130 ms Beats 55.36% 
   Memory 13.9 MB Beats 67.44%

2. Runtime 121 ms Beats 72.45% 
   Memory 13.8 MB Beats 67.44%
"""
