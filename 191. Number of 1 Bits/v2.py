import collections


class Solution:
    def hammingWeight(self, n):
        counter = collections.Counter(bin(n)[2:])
        return counter.get("1", 0)


def main():
    s = Solution()
    print(s.hammingWeight('00000000000000000000000000001011'))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 35 ms, faster than 88.63% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.8 MB, less than 50.90% of Python3 online submissions for Number of 1 Bits.

2. Runtime: 64 ms, faster than 14.12% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.9 MB, less than 50.90% of Python3 online submissions for Number of 1 Bits.
"""
