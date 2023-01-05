class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        result, arrow_position = 0, 0

        for start, end in sorted(points, key=lambda x: x[1]):
            if result == 0 or start > arrow_position:
                result, arrow_position = result + 1, end

        return result


def main():
    s = Solution()
    print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 3196 ms Beats 33.42% 
   Memory 59.8 MB Beats 70.29%

2. Runtime 3054 ms Beats 39.46% 
   Memory 59.8 MB Beats 70.29%
"""
