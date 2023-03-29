class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        res = total = 0

        satisfaction.sort()

        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total

        return res


def main():
    s = Solution()
    print(s.maxSatisfaction([-1, -8, 0, 5, -9]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 44 ms Beats 64.24% 
   Memory 14 MB Beats 46.84%

2. Runtime 32 ms Beats 98.10% 
   Memory 14 MB Beats 46.84%
"""
