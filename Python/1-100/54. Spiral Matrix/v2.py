class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


def main():
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 30 ms Beats 79.78% 
   Memory 13.9 MB Beats 74.53%

2. Runtime 33 ms Beats 61.87% 
   Memory 13.9 MB Beats 25.13%
"""
