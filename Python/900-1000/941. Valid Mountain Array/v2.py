class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        i, j, n = 0, len(arr) - 1, len(arr)

        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1

        return 0 < i == j < n - 1


def main():
    s = Solution()
    print(s.validMountainArray([0, 1, 2, 3, 2, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 206 ms Beats 89.22% 
   Memory 15.3 MB Beats 66%

2. Runtime 198 ms Beats 97.21%
   Memory 15.4 MB Beats 66%
"""
