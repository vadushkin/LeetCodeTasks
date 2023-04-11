class Solution:
    def removeStars(self, s: str) -> str:
        res = []

        for c in s:
            if c != '*':
                res += c
            elif res:
                res.pop()

        return ''.join(res)


def main():
    s = Solution()
    print(s.removeStars("leet**cod*e"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 274 ms Beats 38.71% 
   Memory 15.7 MB Beats 40.9%

2. Runtime 279 ms Beats 37.10% 
   Memory 15.7 MB Beats 40.9%
"""
