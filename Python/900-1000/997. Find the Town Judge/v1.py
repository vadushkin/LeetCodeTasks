class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        count = [0] * (n + 1)

        for i, j in trust:
            count[i] -= 1
            count[j] += 1

        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i

        return -1


def main():
    s = Solution()
    print(s.findJudge(2, [[1, 2]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 783 ms Beats 57.40%
   Memory 19 MB Beats 25.51%

2. Runtime 716 ms Beats 98.7%
   Memory 18.9 MB Beats 59.7%
"""
