class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        while matrix:
            result += matrix.pop(0)

            if matrix and matrix[0]:
                for line in matrix:
                    result.append(line.pop())

            if matrix:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for line in matrix[::-1]:
                    result.append(line.pop(0))

        return result


def main():
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 31 ms Beats 74.80% 
   Memory 13.8 MB Beats 98.75% 

2. Runtime 32 ms Beats 67.9% 
   Memory 13.9 MB Beats 74.53%
"""
