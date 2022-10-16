class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        return sorted(sorted(arr, key=lambda e: (abs(x - e), e))[:k])


def main():
    s = Solution()
    print(s.findClosestElements([1, 2, 3, 4, 5, 6, 7, 8], 3, 4))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 733 ms, faster than 22.28% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 16.1 MB, less than 16.85% of Python3 online submissions for Find K Closest Elements.

2. Runtime: 692 ms, faster than 27.17% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 16.3 MB, less than 11.12% of Python3 online submissions for Find K Closest Elements.
"""
