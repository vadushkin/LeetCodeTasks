class Solution:
    def totalNQueens(self, n: int) -> int:
        total = []

        def dfs(nums: list, index: int) -> None:
            if index == len(nums):
                total.append(1)
                return
            for i in range(len(nums)):
                nums[index] = i
                if valid(nums, index):
                    dfs(nums, index + 1)

        def valid(nums: list, n: int) -> bool:
            for i in range(n):
                if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                    return False
            return True

        dfs([-1] * n, 0)
        return len(total)


def main():
    s = Solution()
    print(s.totalNQueens(4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 94 ms, faster than 49.83% of Python3 online submissions for N-Queens II.
Memory Usage: 13.8 MB, less than 80.29% of Python3 online submissions for N-Queens II.

2. Runtime: 208 ms, faster than 14.53% of Python3 online submissions for N-Queens II.
Memory Usage: 13.9 MB, less than 37.18% of Python3 online submissions for N-Queens II.
"""
