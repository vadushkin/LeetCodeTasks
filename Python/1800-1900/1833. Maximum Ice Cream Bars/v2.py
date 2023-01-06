class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()

        for i in range(len(costs)):
            coins -= costs[i]
            if coins < 0:
                return i

        return i + 1


def main():
    s = Solution()
    print(s.maxIceCream([1, 3, 2, 4, 1], 7))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1959 ms Beats 37.96%
   Memory 28.1 MB Beats 17.54%

2. Runtime 1801 ms Beats 42.15%
   Memory 27.9 MB Beats 61.26%
"""
