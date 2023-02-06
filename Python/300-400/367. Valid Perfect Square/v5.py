class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left <= right:
            mid = left + (right - left) // 2

            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


def main():
    s = Solution()
    print(s.isPerfectSquare(16))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 34 ms Beats 62.50% 
   Memory 13.8 MB Beats 94.91%

2. Runtime 28 ms Beats 87.98% 
   Memory 13.8 MB Beats 94.91%
"""
