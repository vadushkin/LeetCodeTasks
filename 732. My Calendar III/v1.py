from itertools import accumulate
from sortedcontainers import SortedDict


class MyCalendarThree:
    def __init__(self):
        self.lines = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.lines[start] = self.lines.get(start, 0) + 1
        self.lines[end] = self.lines.get(end, 0) - 1
        return max(accumulate(self.lines.values()))


def main():
    s = MyCalendarThree


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1184 ms, faster than 80.61% of Python3 online submissions for My Calendar III.
Memory Usage: 14.9 MB, less than 32.00% of Python3 online submissions for My Calendar III.

2. Runtime: 2442 ms, faster than 47.08% of Python3 online submissions for My Calendar III.
Memory Usage: 14.9 MB, less than 24.31% of Python3 online submissions for My Calendar III.
"""
