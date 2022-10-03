class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        curr_max_time = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                curr_max_time = 0
            total_time += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])
        return total_time


def main():
    s = Solution()
    print(s.minCost("aabaa", [1, 2, 3, 4, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2935 ms, faster than 16.73% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 25 MB, less than 52.92% of Python3 online submissions for Minimum Time to Make Rope Colorful.

2. Runtime: 3079 ms, faster than 11.62% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 24.9 MB, less than 74.83% of Python3 online submissions for Minimum Time to Make Rope Colorful.
"""
