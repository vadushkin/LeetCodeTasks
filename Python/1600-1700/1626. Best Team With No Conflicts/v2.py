class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        dp = [0] * (1 + max(ages))
        score_age = sorted(zip(scores, ages))

        for score, age in score_age:
            dp[age] = score + max(dp[:age + 1])

        return max(dp)


def main():
    s = Solution()
    print(s.bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 409 ms Beats 92.91% 
   Memory 14.3 MB Beats 51.77%

2. Runtime 418 ms Beats 92.91% 
   Memory 14.2 MB Beats 51.77%
"""
