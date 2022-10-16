class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        i, j = 0, 0
        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1
            total_time += curr_total - curr_max
            i = j
        return total_time


def main():
    s = Solution()
    print(s.minCost("cabbabbbaca", [6, 1, 8, 4, 1, 10, 6, 9, 10, 2, 10]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1325 ms, faster than 82.94% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 25 MB, less than 26.96% of Python3 online submissions for Minimum Time to Make Rope Colorful.

2. Runtime: 1349 ms, faster than 80.41% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 25 MB, less than 26.96% of Python3 online submissions for Minimum Time to Make Rope Colorful.
"""
