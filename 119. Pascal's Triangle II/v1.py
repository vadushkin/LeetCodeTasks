class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = [[].copy() for _ in range(rowIndex + 1)]
        for i in range(1, rowIndex + 2):
            for j in range(i):
                if j == 0 or j == i - 1:
                    ans[i - 1].append(1)
                else:
                    ans[i - 1].append(sum((ans[i - 2][j - 1], ans[i - 2][j])))
        return ans[rowIndex]


def main():
    s = Solution()
    print(s.getRow(4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 51 ms, faster than 44.08% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.7 MB, less than 96.91% of Python3 online submissions for Pascal's Triangle II.

2. Runtime: 41 ms, faster than 72.76% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.9 MB, less than 63.27% of Python3 online submissions for Pascal's Triangle II.
"""
