class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        arr[:] = [x for a in arr for x in ([a] if a else [0, 0])][:len(arr)]


def main():
    s = Solution()
    print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 103 ms Beats 45.90%
   Memory 14.9 MB Beats 63.24%

2. Runtime 79 ms Beats 56.15%
   Memory 15 MB Beats 22.23%    
"""
