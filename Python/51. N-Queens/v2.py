class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    def dfs(self, nums: list, index: int, path: list[str], res: list[list[str]]) -> None:
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                tmp = "." * len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i + 1:]], res)

    def valid(self, nums: list, n: int) -> bool:
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True


def main():
    s = Solution()
    print(s.solveNQueens(4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 314 ms, faster than 13.05% of Python3 online submissions for N-Queens.
Memory Usage: 14.3 MB, less than 84.26% of Python3 online submissions for N-Queens.

2. Runtime: 245 ms, faster than 19.33% of Python3 online submissions for N-Queens.
Memory Usage: 14.3 MB, less than 95.03% of Python3 online submissions for N-Queens.
"""
