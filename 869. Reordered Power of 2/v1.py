import itertools


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if (n > 0) and (n & (n - 1)) == 0:
            return True
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(n)))


def main():
    s = Solution()
    print(s.reorderedPowerOf2(46))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4150 ms, faster than 15.51% of Python3 online submissions for Reordered Power of 2.
Memory Usage: 13.7 MB, less than 96.79% of Python3 online submissions for Reordered Power of 2.

2. Runtime: 4483 ms, faster than 13.90% of Python3 online submissions for Reordered Power of 2.
Memory Usage: 13.7 MB, less than 96.79% of Python3 online submissions for Reordered Power of 2.
"""
