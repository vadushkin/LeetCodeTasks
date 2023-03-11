import collections


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        return sum(value * (value - 1) // 2 for value in
                   collections.Counter(tuple(sorted(domino)) for domino in dominoes).values())


def main():
    s = Solution()
    print(s.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 246 ms Beats 69.7% 
   Memory 23.8 MB Beats 47.42%

2. Runtime 237 ms Beats 89.69% 
   Memory 23.9 MB Beat 23.20%
"""
