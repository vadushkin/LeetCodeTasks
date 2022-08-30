class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])


def main():
    s = Solution()
    print(s.rotate([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 36 ms, faster than 93.87% of Python3 online submissions for Rotate Image.
Memory Usage: 13.9 MB, less than 29.99% of Python3 online submissions for Rotate Image.

2. Runtime: 60 ms, faster than 39.22% of Python3 online submissions for Rotate Image.
Memory Usage: 13.9 MB, less than 74.32% of Python3 online submissions for Rotate Image.
"""
