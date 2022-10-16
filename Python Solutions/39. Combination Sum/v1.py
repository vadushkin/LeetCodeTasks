class Solution:
    def combinationSum(self, candidates, target):
        dp = [[] for i in range(target + 1)]
        for c in candidates:
            for i in range(c, target + 1):
                if i == c:
                    dp[i].append([c])
                for comb in dp[i - c]:
                    dp[i].append(comb + [c])
        return dp[-1]


s = Solution()
print(s.combinationSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50))

"""Tests:
1. Runtime: 105 ms, faster than 73.43% of Python3 online submissions for Combination Sum.
Memory Usage: 15.4 MB, less than 6.14% of Python3 online submissions for Combination Sum.

2. Runtime: 73 ms, faster than 94.71% of Python3 online submissions for Combination Sum.
Memory Usage: 15.3 MB, less than 6.14% of Python3 online submissions for Combination Sum.

3. Runtime: 96 ms, faster than 81.14% of Python3 online submissions for Combination Sum.
Memory Usage: 15.3 MB, less than 6.14% of Python3 online submissions for Combination Sum.
"""