class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        orig = {}
        sub = {}

        for edge in edges:
            if edge[0] in orig and edge[1] in orig:
                if orig[edge[0]] != orig[edge[1]]:
                    sub[orig[edge[0]]] += sub[orig[edge[1]]]
                    tmp = orig[edge[1]]

                    for i in sub[orig[edge[1]]]:
                        orig[i] = orig[edge[0]]

                    sub.pop(tmp)
                    orig[edge[1]] = orig[edge[0]]

            elif edge[0] in orig:
                orig[edge[1]] = orig[edge[0]]
                sub[orig[edge[0]]].append(edge[1])
            elif edge[1] in orig:
                orig[edge[0]] = orig[edge[1]]
                sub[orig[edge[1]]].append(edge[0])
            else:
                orig[edge[0]] = edge[0]
                orig[edge[1]] = edge[0]
                sub[edge[0]] = [edge[0], edge[1]]

        summary = 0
        nn = n

        for exc in range(n):
            if exc not in orig:
                nn -= 1
                summary += nn

        for k in sub.keys():
            summary += (nn - len(sub[k])) * len(sub[k])
            nn -= len(sub[k])

        return summary


def main():
    s = Solution()
    print(s.countPairs(3, [[0, 1], [0, 2], [1, 2]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1993 ms Beats 97.86% 
   Memory 73.9 MB Beats 81.14%

2. Runtime 2054 ms Beats 90.4% 
   Memory 73.9 MB Beats 85.5%
"""
