class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        s, e = new_interval[0], new_interval[1]
        left, right = [], []

        for i in intervals:
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])

        return left + [[s, e]] + right


def main():
    s = Solution()
    s.insert([[1, 3], [6, 9]], [2, 5])


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 73 ms Beats 98.66%
   Memory 17.5 MB Beats 24.85%

2. Runtime 86 ms Beats 75.67% 
   Memory 17.6 MB Beats 6.88%
"""
