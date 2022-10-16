class Solution:
    def hammingWeight(self, n: int) -> int:
        s = '{0:032b}'.format(n)
        d = 0
        for i in s:
            if i == '1':
                d += 1
        return d


def main():
    s = Solution()
    print(s.hammingWeight('00000000000000000000000000001011'))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 33 ms, faster than 91.99% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.8 MB, less than 50.90% of Python3 online submissions for Number of 1 Bits.

2. Runtime: 56 ms, faster than 31.81% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.9 MB, less than 50.90% of Python3 online submissions for Number of 1 Bits.
"""
