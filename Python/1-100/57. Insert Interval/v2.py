class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        ans = []
        i = 0

        while i < len(intervals) and new_interval[0] > intervals[i][1]:
            ans.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(intervals[i][0], new_interval[0])
            new_interval[1] = max(intervals[i][1], new_interval[1])
            i += 1

        ans.append(new_interval)

        while i < len(intervals):
            ans.append(intervals[i])
            i += 1

        return ans


def main():
    s = Solution()
    s.insert([[1, 3], [6, 9]], [2, 5])


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 86 ms Beats 75.67%
   Memory 17.3 MB Beats 91.18%

2. Runtime 87 ms Beats 72.71%
   Memory 17.3 MB Beats 91.18%
"""
