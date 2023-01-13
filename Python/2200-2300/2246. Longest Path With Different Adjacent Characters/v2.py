from heapq import nlargest


class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        children = [[] for _ in range(len(s))]

        for i, j in enumerate(parent):
            if j >= 0:
                children[j].append(i)

        res = [0]

        def dfs(x):
            candi = [0]

            for y in children[x]:
                cur = dfs(y)
                if s[x] != s[y]:
                    candi.append(cur)

            candi = nlargest(2, candi)
            res[0] = max(res[0], sum(candi) + 1)

            return max(candi) + 1

        dfs(0)
        return res[0]


def main():
    s = Solution()
    print(s.longestPath([-1, 0, 0, 1, 1, 2], "abacbe"))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 2351 ms Beats 69.44%
   Memory 151.8 MB Beats 56.88%
   
2. Runtime 2234 ms Beats 72.27% 
   Memory 151.8 MB Beats 56.88% 
"""
