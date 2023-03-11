import collections


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        answer = 0
        counter = collections.Counter()

        for domino_a, domino_b in dominoes:
            answer += counter[(domino_a, domino_b)]

            if domino_a != domino_b:
                answer += counter[(domino_b, domino_a)]

            counter[(domino_a, domino_b)] += 1

        return answer


def main():
    s = Solution()
    print(s.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 235 ms Beats 94.7% 
   Memory 23.6 MB Beats 78.35%

2. Runtime 249 ms Beats 61.86% 
   Memory 23.6 MB Beats 78.35%
"""
