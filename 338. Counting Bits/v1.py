class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n + 1):
            ans.append(sum([int(a) for a in str(bin(i)[2:])]))
        return ans


def main():
    s = Solution()
    print(s.countBits(26))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 723 ms, faster than 5.01% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 78.91% of Python3 online submissions for Counting Bits.

2. Runtime: 409 ms, faster than 9.75% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 78.91% of Python3 online submissions for Counting Bits.
"""
