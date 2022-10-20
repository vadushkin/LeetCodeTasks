class MyCalendarThree:

    def __init__(self):
        self.max_over_laps = 1
        self.intervals = []

    def book(self, start: int, end: int) -> int:
        self.intervals.append((start, +1))
        self.intervals.append((end, -1))

        self.intervals.sort()

        curr_max = 0
        for i in self.intervals:
            curr_max += i[1]
            self.max_over_laps = max(self.max_over_laps, curr_max)

        return self.max_over_laps


def main():
    s = MyCalendarThree()


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2769 ms, faster than 37.84% of Python3 online submissions for My Calendar III.
Memory Usage: 14.3 MB, less than 92.31% of Python3 online submissions for My Calendar III.

2. Runtime: 1728 ms, faster than 68.92% of Python3 online submissions for My Calendar III.
Memory Usage: 14.3 MB, less than 77.23% of Python3 online submissions for My Calendar III.
"""
