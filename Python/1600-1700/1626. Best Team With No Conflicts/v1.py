class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        scores = [(ages[i], scores[i]) for i in range(len(scores))]
        scores = sorted(scores, key=lambda x: (x[0], x[1]))

        dp = [scores[i][1] for i in range(len(scores))]
        ans = dp[0]

        for i in range(len(scores)):
            score = scores[i][1]

            for j in range(i):
                if scores[j][1] <= score:
                    dp[i] = max(dp[i], score + dp[j])
                    ans = max(dp[i], ans)

        return ans


def main():
    s = Solution()
    print(s.bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 2397 ms Beats 43.26%
   Memory 14.3 MB Beats 22.70%

2. Runtime 2404 ms Beats 43.26%
   Memory 14.2 MB Beats 83.69%
"""
