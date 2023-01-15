class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        i = 0

        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1


def main():
    s = Solution()
    print(s.validMountainArray([0, 1, 2, 3, 2, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 208 ms Beats 85.81% 
   Memory 15.5 MB Beats 19.42%

2. Runtime 215 ms Beats 72.55%
   Memory 15.3 MB Beats 97.82%
"""
