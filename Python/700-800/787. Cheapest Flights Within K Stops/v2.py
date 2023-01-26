import collections


class Solution:
    def findCheapestPrice(self, _: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        if len(flights) == 1 and flights[0][0] == src and flights[0][1] == dst:
            return flights[0][2]
        elif len(flights) == 1:
            return -1

        adj = collections.defaultdict(list)

        for u, v, cost in flights:
            adj[u].append((v, cost))

        q = collections.deque([(src, 0)])
        left = 0
        gl_cost = len(flights) * [float('inf')]

        while q and left <= k:
            len_q = len(q)

            for i in range(len_q):
                node, cost = q.popleft()

                for v, v_cost in adj[node]:
                    if gl_cost[v] > cost + v_cost:
                        gl_cost[v] = cost + v_cost
                        q.append((v, gl_cost[v]))

            left += 1

        return gl_cost[dst] if gl_cost[dst] < float('inf') else -1


def main():
    s = Solution()
    print(s.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 100 ms Beats 96.20%
   Memory 15.2 MB Beats 54.38%

2. Runtime 100 ms Beats 96.20% 
   Memory 15.4 MB Beats 37.88%
"""
