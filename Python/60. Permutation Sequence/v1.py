"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        self.dfs(list(range(1, n + 1)), [], res, k)
        return "".join(res[k - 1])

    def dfs(self, nums, path, res, k):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            n = nums[:i] + nums[i + 1:]
            p = path + [str(nums[i])]
            self.dfs(n, p, res, k)

# TimeError
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(n: int) -> int:
            r = 1
            for i in range(2, n + 1):
                r *= i
            return r

        nums = [str(i) for i in range(1, n + 1)]
        s = ''
        while nums:
            div = fact(len(nums) - 1)
            idx = 0
            while k > div:
                idx += 1
                k -= div
            s += nums.pop(idx)
        return s


def main():
    s = Solution()
    print(s.getPermutation(3, 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 46 ms, faster than 71.02% of Python3 online submissions for Permutation Sequence.
Memory Usage: 13.9 MB, less than 33.63% of Python3 online submissions for Permutation Sequence.

2. Runtime: 72 ms, faster than 20.44% of Python3 online submissions for Permutation Sequence.
Memory Usage: 14 MB, less than 33.63% of Python3 online submissions for Permutation Sequence.
"""
