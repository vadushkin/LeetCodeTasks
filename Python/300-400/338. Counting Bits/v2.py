class Solution:
    def countBits(self, num: int) -> list[int]:
        counter = [0]
        for i in range(1, num + 1):
            counter.append(counter[i >> 1] + i % 2)
        return counter


def main():
    s = Solution()
    print(s.countBits(5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 79 ms, faster than 97.58% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 78.91% of Python3 online submissions for Counting Bits.

2. Runtime: 195 ms, faster than 39.86% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 78.91% of Python3 online submissions for Counting Bits.
"""
