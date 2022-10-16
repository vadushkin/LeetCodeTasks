"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return sum([1 for i in range(low, high + 1) if i % 2 != 0])


# TimeError
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


def main():
    s = Solution()
    print(s.countOdds(3, 7))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 31.50% of Python3 online submissions for Count Odd Numbers in an Interval Range.
Memory Usage: 13.8 MB, less than 58.97% of Python3 online submissions for Count Odd Numbers in an Interval Range.

2. Runtime: 64 ms, faster than 10.69% of Python3 online submissions for Count Odd Numbers in an Interval Range.
Memory Usage: 13.9 MB, less than 10.98% of Python3 online submissions for Count Odd Numbers in an Interval Range.
"""
