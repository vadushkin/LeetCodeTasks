class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses_count = [-1] * 100001

        for winner, loser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[loser] == -1:
                losses_count[loser] = 1
            else:
                losses_count[loser] += 1

        answer = [[], []]

        for i in range(100001):
            if losses_count[i] == 0:
                answer[0].append(i)
            elif losses_count[i] == 1:
                answer[1].append(i)

        return answer


def main():
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6],
                         [5, 7], [4, 5], [4, 8], [4, 9],
                         [10, 4], [10, 9]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 3148 ms Beats 72.6% 
   Memory 70.6 MB Beats 8.18%

2. Runtime 7569 ms Beats 5.6%
   Memory 69.5 MB Beats 20.4%
"""
