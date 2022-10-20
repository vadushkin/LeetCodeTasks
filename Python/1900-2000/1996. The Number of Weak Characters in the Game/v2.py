from operator import itemgetter


class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=itemgetter(0), reverse=True)

        cur_attack = properties[0][0]
        prev_best_defense = 0
        cur_best_defense = 0

        res = 0

        for attack, defense in properties:
            if attack != cur_attack:
                prev_best_defense = cur_best_defense
                cur_attack = attack

            cur_best_defense = max(cur_best_defense, defense)

            if defense < prev_best_defense:
                res += 1

        return res


def main():
    s = Solution()
    print(s.numberOfWeakCharacters([[1, 2], [3, 2], [4, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4395 ms, faster than 15.89% of Python3 online submissions for The Number of Weak Characters in the Game.
Memory Usage: 68.2 MB, less than 34.99% of Python3 online submissions for The Number of Weak Characters in the Game.

2. Runtime: 4480 ms, faster than 14.48% of Python3 online submissions for The Number of Weak Characters in the Game.
Memory Usage: 68.1 MB, less than 38.48% of Python3 online submissions for The Number of Weak Characters in the Game.
"""
