import numpy as np


class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for i in range(4):
            if np.allclose(mat, target):
                return True
            mat = np.rot90(mat)

        return False


def main():
    s = Solution()
    print(s.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 293 ms, faster than 5.18% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
Memory Usage: 32 MB, less than 5.08% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.

2. Runtime: 294 ms, faster than 5.18% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
Memory Usage: 31.9 MB, less than 5.08% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
"""
