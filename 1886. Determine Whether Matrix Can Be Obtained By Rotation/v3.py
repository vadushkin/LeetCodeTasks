class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        if (mat == target or
                mat == [list(c)[::-1] for c in zip(*target)] or
                mat == [list(c) for c in zip(*target)][::-1] or
                mat == [r[::-1] for r in target][::-1]):
            return True

        return False


def main():
    s = Solution()
    print(s.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 82 ms, faster than 23.51% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
Memory Usage: 13.9 MB, less than 78.49% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.

2. Runtime: 56 ms, faster than 75.10% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
Memory Usage: 13.9 MB, less than 78.49% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
"""
