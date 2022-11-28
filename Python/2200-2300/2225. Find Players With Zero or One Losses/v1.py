class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = {e: 0 for q in matches for e in q}

        for i in range(len(matches)):
            players[matches[i][1]] += 1

        return [[w[0] for w in sorted(players.items()) if w[1] == 0],
                [w[0] for w in sorted(players.items()) if w[1] == 1]]


def main():
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
                         [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 5681 ms Beats 7.40%
   Memory 68.3 MB Beats 88.94%
 
2. Runtime 5933 ms Beats 5.86%
   Memory 68.8 MB Beats 77.41%
"""


# improved version
class Solution2:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = {e: 0 for q in matches for e in q}

        for i in range(len(matches)):
            players[matches[i][1]] += 1

        zero_list = []
        one_list = []

        for w in sorted(players.items()):
            if w[1] == 0:
                zero_list.append(w[0])
            elif w[1] == 1:
                one_list.append(w[0])

        return [zero_list, one_list]


def main():
    s = Solution2()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
                         [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2026 ms Beats 84.66%
   Memory 68.8 MB Beats 77.41%

2. Runtime 5044 ms Beats 15.24%
   Memory 68.7 MB Beats 77.41%
"""
