class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses_count = {}

        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] = losses_count.get(loser, 0) + 1

        zero_lose, one_lose = [], []

        for player, count in losses_count.items():
            if count == 0:
                zero_lose.append(player)
            if count == 1:
                one_lose.append(player)

        return [sorted(zero_lose), sorted(one_lose)]


def main():
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6],
                         [5, 7], [4, 5], [4, 8], [4, 9],
                         [10, 4], [10, 9]]))


if __name__ == "__main__":
    main()

""""Tests:
1. Runtime 4900 ms Beats 19.59%
   Memory 69 MB Beats 41.15%

2. Runtime 4466 ms Beats 46.33% 
   Memory 68.8 MB Beats 58.91%
"""
