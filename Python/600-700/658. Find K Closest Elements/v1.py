class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]


def main():
    s = Solution()
    print(s.findClosestElements([1, 2, 3, 4, 5], 3, 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 795 ms, faster than 15.55% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.5 MB, less than 80.93% of Python3 online submissions for Find K Closest Elements.

2. Runtime: 293 ms, faster than 97.62% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.5 MB, less than 45.71% of Python3 online submissions for Find K Closest Elements.
"""
