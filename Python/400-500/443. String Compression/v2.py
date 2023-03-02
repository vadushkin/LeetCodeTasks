from functools import reduce
from itertools import groupby


class Solution:
    def compress(self, chars: list[str]) -> int:
        return reduce(lambda i, c: (lambda s: chars.__setitem__(slice(i, i + len(s)), s) or i + len(s))(
            c[0] + str(('', c[1])[c[1] > 1])), ((c, sum(1 for _ in g)) for c, g in groupby(chars)), 0)


def main():
    s = Solution()
    print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 63 ms Beats 58.40% 
   Memory 13.8 MB Beats 96.79%

2. Runtime 62 ms Beats 63.96% 
   Memory 14.1 MB Beats 25.81%
"""
