class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n, pos = len(s), -float('inf')
        res = [n] * n

        for i in list(range(n)) + list(range(n)[::-1]):
            if s[i] == c:
                pos = i

            res[i] = min(res[i], abs(i - pos))

        return res


def main():
    s = Solution()
    print(s.shortestToChar("loveleetcode", "e"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 39 ms Beats 95.18%
   Memory 13.9 MB Beats 53.34%

2. Runtime 39 ms Beats 95.18%
   Memory 13.9 MB Beats 53.34%
"""
