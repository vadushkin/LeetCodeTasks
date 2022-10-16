class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]


def main():
    s = Solution()
    print(s.summaryRanges([0, 2, 4, 5, 6]))


if __name__ == "__main__":
    main()

""""Tests:
1. Runtime: 43 ms, faster than 63.24% of Python3 online submissions for Summary Ranges.
Memory Usage: 13.9 MB, less than 21.89% of Python3 online submissions for Summary Ranges.

2. Runtime: 36 ms, faster than 83.14% of Python3 online submissions for Summary Ranges.
Memory Usage: 14 MB, less than 21.89% of Python3 online submissions for Summary Ranges.
"""
