import math


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        sqrt = int(math.sqrt(area))
        for i in range(sqrt, 0, -1):
            if area % i != 0:
                continue
            return [area // i, i]
        return []


def main():
    s = Solution()
    print(s.constructRectangle(4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 34 ms, faster than 95.00% of Python3 online submissions for Construct the Rectangle.
Memory Usage: 13.9 MB, less than 14.57% of Python3 online submissions for Construct the Rectangle.

2. Runtime: 59 ms, faster than 55.26% of Python3 online submissions for Construct the Rectangle.
Memory Usage: 13.9 MB, less than 58.62% of Python3 online submissions for Construct the Rectangle.

3. Runtime: 58 ms, faster than 57.07% of Python3 online submissions for Construct the Rectangle.
Memory Usage: 13.8 MB, less than 96.81% of Python3 online submissions for Construct the Rectangle.
"""
