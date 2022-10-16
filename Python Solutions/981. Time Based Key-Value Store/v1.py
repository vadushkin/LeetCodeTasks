class TimeMap:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_time_map:
            self.key_time_map[key] = {}

        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_time_map:
            return ""

        for curr_time in reversed(range(1, timestamp + 1)):
            if curr_time in self.key_time_map[key]:
                return self.key_time_map[key][curr_time]

        return ""


def main():
    s = TimeMap()
    # print(s.set())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1720 ms, faster than 30.72% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 69.9 MB, less than 90.76% of Python3 online submissions for Time Based Key-Value Store.

2. Runtime: 1569 ms, faster than 37.81% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 69.9 MB, less than 90.76% of Python3 online submissions for Time Based Key-Value Store.
"""
