import math


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        k, n = num_people, candies
        alloc = [0] * k
        final = (0, 0)

        for i in range(1, k + 1):
            s = ((-1 - 2 * i) + math.sqrt(1 + 8 * n)) / (2 * k)
            t = math.floor(s)
            alloc[i - 1] = i * (t + 1) + k * t * (t + 1) // 2
            final = max(final, (s - math.floor(s), i))

        alloc[final[1] - 1] += (n - sum(alloc))

        return alloc


def main():
    s = Solution()
    print(s.distributeCandies(7, 4))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 49 ms Beats 54.38%
   Memory 14 MB Beats 47.94%

2. Runtime 32 ms Beats 97.16% 
   Memory 13.9 MB Beats 47.94%
"""
