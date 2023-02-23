class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


def main():
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 72 ms Beats 19.67% 
   Memory 14 MB Beats 33.43%
 
2. Runtime 63 ms Beats 54.98% 
   Memory 13.9 MB Beats 96.4%
"""