class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        arr = [-1 for _ in range(71)]
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            j = [x for x in arr[temperatures[i] - 30 + 1:] if x > -1]
            res[i] = 0 if len(j) == 0 else min(j) - i
            arr[temperatures[i] - 30] = i

        return res


def main():
    s = Solution()
    print(s.dailyTemperatures([30, 40, 50, 60]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 5081 ms Beats 5.1% 
   Memory 29.5 MB Beats 22.28%

2. Runtime 2682 ms Beats 59.24% 
   Memory 29.6 MB Beats 22.28% 
"""
