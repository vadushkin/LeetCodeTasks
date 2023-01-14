import collections


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, base_str: str) -> str:
        neighbors = collections.defaultdict(set)

        for a, b in zip(s1, s2):
            neighbors[a].add(b)
            neighbors[b].add(a)

        def dfs(ch, min_char, visited):
            visited.add(ch)
            res = min_char

            for nei in neighbors[ch]:
                if nei not in visited:
                    res = min(res, dfs(nei, min(min_char, nei), visited))

            return res

        return ''.join([dfs(c, c, set()) for c in base_str])


def main():
    s = Solution()
    print(s.smallestEquivalentString("parker", "morris", "parser"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 100 ms Beats 21.26%
   Memory 14.1 MB Beats 6.90%

2. Runtime 100 ms Beats 21.26%
   Memory 14.2 MB Beats 6.90%
"""
