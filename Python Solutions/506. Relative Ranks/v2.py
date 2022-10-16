class Solution:
    def findRelativeRanks(self, nums):
        rank = {n: i > 2 and str(i + 1) or
                   ["Gold", "Silver", "Bronze"][i] + ' Medal'
                for i, n in enumerate(sorted(nums, reverse=True))}
        return [rank[num] for num in nums]


def main():
    s = Solution()
    print(s.findRelativeRanks([3, 10, 5, 4, 6, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 79 ms, faster than 90.84% of Python3 online submissions for Relative Ranks.
Memory Usage: 15 MB, less than 71.59% of Python3 online submissions for Relative Ranks.

2. Runtime: 145 ms, faster than 59.16% of Python3 online submissions for Relative Ranks.
Memory Usage: 15.2 MB, less than 33.83% of Python3 online submissions for Relative Ranks.
"""
