from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        if len(digits) == 0:
            return res

        self.dfs(digits, 0, dic, '', res)
        return res

    def dfs(self, nums, index, dic, path, res):
        if index >= len(nums):
            res.append(path)
            return
        string1 = dic[nums[index]]
        for i in string1:
            self.dfs(nums, index + 1, dic, path + i, res)


def main():
    s = Solution()
    print(s.letterCombinations("2345"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 53 ms, faster than 36.01% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.7 MB, less than 99.91% of Python3 online submissions for Letter Combinations of a Phone Number.

2. Runtime: 35 ms, faster than 86.34% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.8 MB, less than 79.63% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
