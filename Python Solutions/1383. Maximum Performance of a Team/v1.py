import heapq


class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        people = sorted(zip(speed, efficiency), key=lambda x: -x[1])

        result, sum_speed = 0, 0
        min_heap = []

        for i, (s, e) in enumerate(people):
            if i < k:
                sum_speed += s
                heapq.heappush(min_heap, s)
            elif s > min_heap[0]:
                sum_speed += s - heapq.heappushpop(min_heap, s)
            else:
                continue

            result = max(result, sum_speed * e)

        return result % (10 ** 9 + 7)


def main():
    s = Solution()
    print(s.maxPerformance(5, [5, 4, 3, 0, 6], [5, 4, 3, 3, 4], 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1001 ms, faster than 5.91% of Python3 online submissions for Maximum Performance of a Team.
Memory Usage: 33.7 MB, less than 21.10% of Python3 online submissions for Maximum Performance of a Team.

2. Runtime: 877 ms, faster than 15.62% of Python3 online submissions for Maximum Performance of a Team.
Memory Usage: 33.6 MB, less than 21.10% of Python3 online submissions for Maximum Performance of a Team.
"""
