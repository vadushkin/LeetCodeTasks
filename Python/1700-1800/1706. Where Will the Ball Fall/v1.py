class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])

        def test(i):
            for j in range(m):
                i2 = i + grid[j][i]
                if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]:
                    return -1
                i = i2
            return i

        return map(test, range(n))


def main():
    s = Solution()
    print(s.findBall([
        [1, 1, 1, -1, -1],
        [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 356 ms, faster than 70.33% of Python3 online submissions for Where Will the Ball Fall.
Memory Usage: 14.3 MB, less than 55.41% of Python3 online submissions for Where Will the Ball Fall.

2. Runtime: 539 ms, faster than 27.53% of Python3 online submissions for Where Will the Ball Fall.
Memory Usage: 14.2 MB, less than 84.52% of Python3 online submissions for Where Will the Ball Fall.
"""
