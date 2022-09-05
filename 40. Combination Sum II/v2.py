class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        def backtrack(nums, targetLeft, path):

            if targetLeft == 0:
                res.append(path)
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > targetLeft:
                    break
                backtrack(nums[i + 1:], targetLeft - nums[i], path + [nums[i]])

        res = []
        backtrack(sorted(candidates), target, [])
        return res


def main():
    s = Solution()
    print(s.combinationSum2([1, 2, 2, 2, 5], 5))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 51 ms, faster than 96.92% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.9 MB, less than 93.24% of Python3 online submissions for Combination Sum II.

2. Runtime: 94 ms, faster than 69.78% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.9 MB, less than 60.01% of Python3 online submissions for Combination Sum II.
"""
