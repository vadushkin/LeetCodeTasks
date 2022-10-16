import math


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        answer_dict = {}
        temp = [float('inf'), float('-inf')]
        for n in range(1, int(math.sqrt(area)) + 1):
            if area % n == 0:
                answer_dict[n] = area // n
        for k, v in answer_dict.items():
            if abs(temp[0] - temp[1]) > abs(k - v):
                temp[0], temp[1] = max(k, v), min(k, v)
        return temp


def main():
    s = Solution()
    print(s.constructRectangle(37))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 69 ms, faster than 36.72% of Python3 online submissions for Construct the Rectangle.
Memory Usage: 13.8 MB, less than 58.62% of Python3 online submissions for Construct the Rectangle.

2. Runtime: 55 ms, faster than 61.55% of Python3 online submissions for Construct the Rectangle.
Memory Usage: 13.9 MB, less than 14.57% of Python3 online submissions for Construct the Rectangle.
"""
