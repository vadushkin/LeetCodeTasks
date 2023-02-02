class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        summary = 0

        for i in range(len(grid[0])):
            max_counts = []

            for j in range(len(grid)):
                value = max(grid[j])
                max_counts.append(value)
                grid[j].remove(value)

            summary += max(max_counts)

        return summary


def main():
    s = Solution()
    print(s.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 134 ms Beats 61.64%
   Memory 13.9 MB Beats 91.94%

2. Runtime 132 ms Beats 62.77%
   Memory 13.9 MB Beats 57.83%
"""
