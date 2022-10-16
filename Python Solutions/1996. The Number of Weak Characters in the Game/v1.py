class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        curr_max = 0
        for _, d in properties:
            if d < curr_max:
                ans += 1
            else:
                curr_max = d
        return ans


def main():
    s = Solution()
    print(s.numberOfWeakCharacters([[1, 2], [2, 3], [3, 4]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 5106 ms, faster than 5.34% of Python3 online submissions for The Number of Weak Characters in the Game.
Memory Usage: 67.2 MB, less than 63.30% of Python3 online submissions for The Number of Weak Characters in the Game.

2. Runtime: 4786 ms, faster than 9.21% of Python3 online submissions for The Number of Weak Characters in the Game.
Memory Usage: 67.1 MB, less than 63.30% of Python3 online submissions for The Number of Weak Characters in the Game.
"""
