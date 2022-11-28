class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        zero_loss = set()
        one_loss = set()
        more_losses = set()

        for winner, loser in matches:
            if (winner not in one_loss) and (winner not in more_losses):
                zero_loss.add(winner)

            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            elif loser in more_losses:
                continue
            else:
                one_loss.add(loser)

        return [sorted(list(zero_loss)), sorted(list(one_loss))]


def main():
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6],
                         [5, 7], [4, 5], [4, 8], [4, 9],
                         [10, 4], [10, 9]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1902 ms Beats 94.37%
   Memory 68.9 MB Beats 41.15%

2. Runtime 4704 ms Beats 30.99%
   Memory 68.9 MB Beats 58.91%
"""
