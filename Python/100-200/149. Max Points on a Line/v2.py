from collections import Counter


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        answer = 0

        for i, (x0, y0) in enumerate(points[:-1]):
            cnt = Counter(((x - x0) / (y - y0) if (y - y0) != 0 else None) for x, y in points[i + 1:])
            answer = max(answer, max(cnt.values()))

        return answer + 1


def main():
    s = Solution()
    print(s.maxPoints([[1, 1], [2, 2], [3, 3]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 56 ms Beats 99.58% 
   Memory 13.9 MB Beats 75.79%

2. Runtime 64 ms Beats 98.9% 
   Memory 13.9 MB Beats 75.79%
"""
