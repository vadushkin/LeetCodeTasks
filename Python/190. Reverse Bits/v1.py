class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str = '{0:032b}'.format(n)
        reverse_str = bit_str[::-1]
        return int(reverse_str, 2)


def main():
    s = Solution()
    print(s.reverseBits('0000010100101000001111010011100'))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 31 ms, faster than 96.65% of Python3 online submissions for Reverse Bits.
Memory Usage: 13.8 MB, less than 49.77% of Python3 online submissions for Reverse Bits.

2. Runtime: 31 ms, faster than 96.65% of Python3 online submissions for Reverse Bits.
Memory Usage: 13.8 MB, less than 94.11% of Python3 online submissions for Reverse Bits.
"""
