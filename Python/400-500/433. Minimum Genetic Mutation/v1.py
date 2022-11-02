from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps

            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)

        return -1


def main():
    s = Solution()
    print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 57 ms, faster than 46.15% of Python3 online submissions for Minimum Genetic Mutation.
Memory Usage: 13.9 MB, less than 37.43% of Python3 online submissions for Minimum Genetic Mutation.
 
2. Runtime: 46 ms, faster than 71.89% of Python3 online submissions for Minimum Genetic Mutation.
Memory Usage: 13.9 MB, less than 37.43% of Python3 online submissions for Minimum Genetic Mutation.
"""
