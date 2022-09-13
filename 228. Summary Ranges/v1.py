class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []

        if not nums:
            return []

        start = nums[0]

        for i in range(len(nums)):

            if i == len(nums) - 1:
                if nums[i] == nums[i - 1] + 1:
                    ans.append(f"{start}->{nums[i]}")
                    break
                ans.append(f"{start}")
                break

            if nums[i + 1] == nums[i] + 1:
                continue

            if nums[i - 1] != nums[i] - 1:
                ans.append(f"{nums[i]}")
            else:
                ans.append(f"{start}->{nums[i]}")

            start = nums[i + 1]

        return ans


def main():
    s = Solution()
    print(s.summaryRanges([0, 2, 4, 6, 8, 9, 10, 11, 23, 44, 41]))


if __name__ == "__main__":
    main()

""""Tests:
1. Runtime: 43 ms, faster than 63.24% of Python3 online submissions for Summary Ranges.
Memory Usage: 13.9 MB, less than 72.78% of Python3 online submissions for Summary Ranges.

2. Runtime: 29 ms, faster than 96.43% of Python3 online submissions for Summary Ranges.
Memory Usage: 13.8 MB, less than 72.78% of Python3 online submissions for Summary Ranges.
"""
