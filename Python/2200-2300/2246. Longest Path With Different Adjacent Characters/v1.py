from collections import defaultdict


class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        mapping = defaultdict(list)

        for x in range(1, len(parent)):
            mapping[parent[x]].append(x)

        def dfs(node):
            total = 1
            largest_sub_path = second_largest_sub_path = 0

            for child in mapping[node]:
                sub_total, sub_path = dfs(child)

                if s[node] != s[child]:
                    if sub_path > largest_sub_path:
                        largest_sub_path, second_largest_sub_path = sub_path, largest_sub_path
                    elif sub_path > second_largest_sub_path:
                        second_largest_sub_path = sub_path

                total = max(sub_total, total)

            total = max(total, largest_sub_path + second_largest_sub_path + 1)

            return total, largest_sub_path + 1

        return dfs(0)[0]


def main():
    s = Solution()
    print(s.longestPath([-1, 0, 0, 1, 1, 2], "abacbe"))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 1991 ms Beats 78.14% 
   Memory 153 MB Beats 45.75%

2. Runtime 1936 ms Beats 79.76%
   Memory 152.8 MB Beats 47.77%
"""
