class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            return (high - low + 1) // 2
        return (high - low) // 2 + 1


def main():
    s = Solution()
    print(s.countOdds(3, 10))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 68 ms, faster than 5.43% of Python3 online submissions for Count Odd Numbers in an Interval Range.
Memory Usage: 14 MB, less than 10.98% of Python3 online submissions for Count Odd Numbers in an Interval Range.

2. Runtime: 58 ms, faster than 25.54% of Python3 online submissions for Count Odd Numbers in an Interval Range.
Memory Usage: 14 MB, less than 10.98% of Python3 online submissions for Count Odd Numbers in an Interval Range.
"""
