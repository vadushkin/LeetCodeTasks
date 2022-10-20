class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[].copy() for _ in range(numRows)]
        for i in range(1, numRows + 1):
            for j in range(i):
                if j == 0 or j == i - 1:
                    ans[i - 1].append(1)
                else:
                    ans[i - 1].append(sum((ans[i - 2][j - 1], ans[i - 2][j])))
        return ans


def main():
    s = Solution()
    print(s.generate(7))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 19 ms, faster than 99.94% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14 MB, less than 17.81% of Python3 online submissions for Pascal's Triangle.

2. Runtime: 41 ms, faster than 70.48% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 65.59% of Python3 online submissions for Pascal's Triangle.
"""
