class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        res = [0 if symbol == c else n for symbol in s]

        for i in range(1, n):
            res[i] = min(res[i], res[i - 1] + 1)

        for i in range(n - 2, -1, -1):
            res[i] = min(res[i], res[i + 1] + 1)

        return res


def main():
    s = Solution()
    print(s.shortestToChar("loveleetcode", "e"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 42 ms Beats 91.24%
   Memory 14 MB Beats 53.34%

2. Runtime 33 ms Beats 98.80%
   Memory 14 MB Beats 53.34%
"""
