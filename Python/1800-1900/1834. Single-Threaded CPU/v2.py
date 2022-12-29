from heapq import heappop, heappush


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        heap, prev, ans = [], 0, []
        tasks = sorted((task, i) for i, task in enumerate(tasks))

        for (enq, pro), i in tasks:
            while heap and prev < enq:
                proj, j, enq_j = heappop(heap)
                prev = max(enq_j, prev) + proj
                ans.append(j)

            heappush(heap, (pro, i, enq))

        return ans + [i for _, i, _ in sorted(heap)]


def main():
    s = Solution()
    print(s.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2074 ms Beats 83.61% 
   Memory 61.7 MB Beats 89.2%

2. Runtime 2059 ms Beats 85.41%
   Memory 61.7 MB Beats 89.2%
"""
