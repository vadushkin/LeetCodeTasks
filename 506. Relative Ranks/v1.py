class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sort = sorted(score)[::-1]
        rank = ["Gold Medal",
                "Silver Medal",
                "Bronze Medal"
                ] + list(map(str, range(4, len(score) + 1)))
        return list(map(dict(zip(sort, rank)).get, score))


def main():
    s = Solution()
    print(s.findRelativeRanks([3, 10, 5, 4, 6, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 160 ms, faster than 49.20% of Python3 online submissions for Relative Ranks.
Memory Usage: 15.1 MB, less than 52.95% of Python3 online submissions for Relative Ranks.

2. Runtime: 140 ms, faster than 63.04% of Python3 online submissions for Relative Ranks.
Memory Usage: 15.1 MB, less than 52.95% of Python3 online submissions for Relative Ranks.
"""
