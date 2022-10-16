class Solution:
    def climbStairs(self, n):
        memo = {1: 1, 2: 2}

        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]

        return climb(n)


s = Solution()
print(s.climbStairs(13))


"""Tests:
1. Runtime: 41 ms, faster than 66.93% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14 MB, less than 11.90% of Python3 online submissions for Climbing Stairs.

2. Runtime: 71 ms, faster than 5.04% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.7 MB, less than 96.27% of Python3 online submissions for Climbing Stairs.

3. Runtime: 37 ms, faster than 78.36% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.9 MB, less than 11.90% of Python3 online submissions for Climbing Stairs.
"""