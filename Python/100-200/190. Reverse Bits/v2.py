class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            if n & 1:
                res += 1 << (31 - i)
            n >>= 1
        return res


def main():
    s = Solution()
    print(s.reverseBits('0000010100101000001111010011100'))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 58 ms, faster than 34.06% of Python3 online submissions for Reverse Bits.
Memory Usage: 13.8 MB, less than 49.77% of Python3 online submissions for Reverse Bits.

2. Runtime: 55 ms, faster than 41.87% of Python3 online submissions for Reverse Bits.
Memory Usage: 13.8 MB, less than 49.77% of Python3 online submissions for Reverse Bits.
"""
