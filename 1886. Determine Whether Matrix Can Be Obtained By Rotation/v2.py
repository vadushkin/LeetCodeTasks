class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        if target == mat:
            return True
        for i in range(3):
            for j in range(len(mat)):
                for k in range(j + 1, len(mat)):
                    mat[j][k], mat[k][j] = mat[k][j], mat[j][k]
                mat[j] = mat[j][::-1]
            if target == mat:
                return True
        return False


def main():
    s = Solution()
    print(s.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 72 ms, faster than 45.72% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
Memory Usage: 13.9 MB, less than 78.49% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.

2. Runtime: 75 ms, faster than 38.65% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
Memory Usage: 13.9 MB, less than 32.97% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
"""
