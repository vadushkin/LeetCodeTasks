class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        s = ''.join(map(chr, range(n)))

        for a, b in connections:
            s = s.replace(s[a], s[b])

        return len(set(s)) - 1


def main():
    s = Solution()
    print(s.makeConnected(4, [[0, 1], [0, 2], [1, 2]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 910 ms Beats 9.77% 
   Memory 34.3 MB Beats 55.64%

2. Runtime 907 ms Beats 10.5% 
   Memory 34.2 MB Beats 61.37%
"""
