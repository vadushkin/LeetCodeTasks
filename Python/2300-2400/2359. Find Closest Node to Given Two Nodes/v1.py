class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        res, min_dist, n = -1, float('inf'), len(edges)
        dist1, dist2 = [-1] * n, [-1] * n

        self.dfs(node1, 0, edges, dist1)
        self.dfs(node2, 0, edges, dist2)

        for i in range(n):
            if min(dist1[i], dist2[i]) >= 0 and max(dist1[i], dist2[i]) < min_dist:
                min_dist = max(dist1[i], dist2[i])
                res = i

        return res

    @staticmethod
    def dfs(node, dist, edges, dis):
        while node != -1 and dis[node] == -1:
            dis[node] = dist
            dist += 1
            node = edges[node]


def main():
    s = Solution()
    print(s.closestMeetingNode([2, 2, 3, -1], 0, 1))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1268 ms Beats 79.89% 
   Memory 29.1 MB Beats 73.56%

2. Runtime 1714 ms Beats 37.93% 
   Memory 29 MB Beats 73.56%
"""
