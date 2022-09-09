class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


def main():
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1479 ms, faster than 6.24% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 27.2 MB, less than 50.72% of Python3 online submissions for Contains Duplicate II.

2. Runtime: 638 ms, faster than 93.94% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 27.2 MB, less than 74.05% of Python3 online submissions for Contains Duplicate II.
"""
