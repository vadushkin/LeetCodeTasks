class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):
                if target < nums[i] * N or target > nums[-1] * N:
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
        return


def main():
    s = Solution()
    print(s.fourSum(
        [1, 2, 3, 4, 5],
        10
    ))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 109 ms, faster than 95.65% of Python3 online submissions for 4Sum.
Memory Usage: 14 MB, less than 63.98% of Python3 online submissions for 4Sum.

2. Runtime: 84 ms, faster than 99.12% of Python3 online submissions for 4Sum.
Memory Usage: 13.9 MB, less than 63.98% of Python3 online submissions for 4Sum.
"""
