class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0

        for c in s:
            if c == '0':
                m += 1

        ans = m

        for c in s:
            if c == '0':
                m -= 1
                ans = min(ans, m)
            else:
                m += 1

        return ans


def main():
    s = Solution()
    print(s.minFlipsMonoIncr("00110"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 174 ms Beats 85.90% 
   Memory 14.9 MB Beats 72.76%
 
2. Runtime 167 ms Beats 86.86%
   Memory 15 MB Beats 53.53%
"""
