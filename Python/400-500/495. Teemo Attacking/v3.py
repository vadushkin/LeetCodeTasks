class Solution:
    def findPoisonedDuration(self, time_series: list[float | int], duration: int) -> int:
        return sum(min(duration, b - a) for a, b in zip(time_series, time_series[1:] + [10e7]))


def main():
    s = Solution()
    print(s.findPoisonedDuration([1, 2, 3, 4, 5], 5))


if __name__ == '__main__':
    main()

"""
Tests: 
1. Runtime 263 ms Beats 76.34% 
   Memory 15.6 MB Beats 9.27%

2. Runtime 248 ms Beats 94.87% 
   Memory 15.5 MB Beats 87.35%
"""
