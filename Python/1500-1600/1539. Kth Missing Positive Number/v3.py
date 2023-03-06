class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            middle = (left + right) // 2

            if arr[middle] - 1 - middle < k:
                left = middle + 1
            else:
                right = middle

        return left + k


def main():
    s = Solution()
    print(s.findKthPositive([2, 3, 4, 7, 11], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 47 ms Beats 91.27% 
   Memory 14 MB Beats 80.43%

2. Runtime 47 ms Beats 91.27% 
   Memory 13.9 MB Beats 80.43%
"""
