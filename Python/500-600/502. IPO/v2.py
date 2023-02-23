class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        m = max(capital)
        n = len(profits)

        while k > 0:
            if k >= n and w >= m:
                return w + sum(profits)

            projects = [i for i in range(n) if capital[i] <= w]

            if not projects:
                break

            index = projects[0]

            for p in projects:
                if profits[p] >= profits[index]:
                    index = p

            capital.pop(index)
            w += profits.pop(index)

            k -= 1
            n -= 1

        return w


def main():
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1041 ms Beats 67.13% 
   Memory 32.8 MB Beats 99.48%

2. Runtime 1076 ms Beats 54.2% 
   Memory 32.4 MB Beats 99.83%
"""
