class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = index = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank, index = 0, i + 1

        return index


def main():
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 684 ms Beats 89.22%
   Memory 19.3 MB Beats 23.25%

2. Runtime 703 ms Beats 80.48%
   Memory 19.2 MB Beats 61.76%
"""
