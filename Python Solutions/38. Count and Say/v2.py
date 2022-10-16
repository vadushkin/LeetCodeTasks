import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
        return s


def main():
    s = Solution()
    print(s.countAndSay(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 91.33% of Python3 online submissions for Count and Say.
Memory Usage: 14 MB, less than 26.80% of Python3 online submissions for Count and Say.

2. Runtime: 90 ms, faster than 23.84% of Python3 online submissions for Count and Say.
Memory Usage: 14 MB, less than 26.80% of Python3 online submissions for Count and Say.
"""
