class Solution:
    def findPoisonedDuration(self, time_series: list[int], duration: int) -> int:
        dp = [0] * time_series[-1] + [0] * (duration - 1)

        for i in range(len(time_series)):
            dp[time_series[i] - 1:time_series[i] - 1 + duration] = [1] * duration

        return sum(dp)


def main():
    s = Solution()
    print(s.findPoisonedDuration([1, 2, 4], 2))


if __name__ == '__main__':
    main()

"""Tests:
1. Time Limit Exceeded 
   22 / 40 testcases passed

2. Time Limit Exceeded 
   22 / 40 testcases passed
"""
