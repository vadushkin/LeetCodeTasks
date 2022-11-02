from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:

        def checkNeighbor(a, b):
            return sum([1 for i in range(len(a)) if a[i] != b[i]]) == 1

        q = deque([start])

        visited = set()
        mutations = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return mutations

                if cur not in visited:
                    visited.add(cur)
                    for nei in bank:
                        if checkNeighbor(cur, nei):
                            q.append(nei)
            mutations += 1

        return -1


def main():
    s = Solution()
    print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 68.20% of Python3 online submissions for Minimum Genetic Mutation.
Memory Usage: 13.9 MB, less than 86.98% of Python3 online submissions for Minimum Genetic Mutation.

2. Runtime: 73 ms, faster than 5.62% of Python3 online submissions for Minimum Genetic Mutation.
Memory Usage: 14 MB, less than 37.43% of Python3 online submissions for Minimum Genetic Mutation.
"""
