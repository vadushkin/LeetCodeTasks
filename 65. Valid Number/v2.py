import re


class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r'^[\-\+]?([0-9]+([\.][0-9]*)?|[\.][0-9]+)([eE][\-\+]?[0-9]+)?$', s.strip()) is not None


def main():
    s = Solution()
    print(s.isNumber("1E9"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 72 ms, faster than 18.57% of Python3 online submissions for Valid Number.
Memory Usage: 14 MB, less than 31.84% of Python3 online submissions for Valid Number.

2. Runtime: 34 ms, faster than 95.78% of Python3 online submissions for Valid Number.
Memory Usage: 13.8 MB, less than 97.87% of Python3 online submissions for Valid Number.
"""
