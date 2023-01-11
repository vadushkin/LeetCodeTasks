class Solution:
    def minTime(self, n: int, edges: list[list[int]], has_apple: list[bool]) -> int:
        parents = [-1] * n

        for edge in edges:
            parent, child = edge

            if parents[child] == -1:
                parents[child] = parent
            else:
                parents[parent] = child

        for h in range(n - 1, 0, -1):
            if has_apple[h] and parents[h] != -1:
                has_apple[parents[h]] = True

        return sum(has_apple[1:]) * 2


def main():
    s = Solution()
    print(s.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                    [False, False, True, False, True, True, False]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 553 ms Beats 100%
   Memory 49.2 MB Beats 97.44%

2. Runtime 570 ms Beats 100% 
   Memory 49.3 MB Beats 97.44%
"""
