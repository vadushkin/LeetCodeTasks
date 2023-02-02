class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map = {}

        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False

                    break

        return True


def main():
    s = Solution()
    print(s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 47 ms Beats 35.69%
   Memory 13.9 MB Beats 31.27%

2. Runtime 36 ms Beats 82.13% 
   Memory 13.9 MB Beats 77.66%
"""
