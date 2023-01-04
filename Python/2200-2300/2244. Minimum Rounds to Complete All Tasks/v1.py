from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        values = Counter(tasks).values()
        return -1 if 1 in values else sum((value + 2) // 3 for value in values)


def main():
    s = Solution()
    print(s.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2326 ms Beats 40.82% 
   Memory 28.2 MB Beats 82.79%

2. Runtime 2376 ms Beats 39.19% 
   Memory 28.3 MB Beats 60.98%
"""
