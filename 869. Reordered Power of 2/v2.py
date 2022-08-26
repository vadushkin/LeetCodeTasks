import collections


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if (n > 0) and (n & (n - 1)) == 0:
            return True
        count = collections.Counter(str(n))
        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))


def main():
    s = Solution()
    print(s.reorderedPowerOf2(46))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 58.82% of Python3 online submissions for Reordered Power of 2.
Memory Usage: 13.8 MB, less than 96.79% of Python3 online submissions for Reordered Power of 2.

2. Runtime: 46 ms, faster than 78.07% of Python3 online submissions for Reordered Power of 2.
Memory Usage: 13.8 MB, less than 96.79% of Python3 online submissions for Reordered Power of 2.
"""
