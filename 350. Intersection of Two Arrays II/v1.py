from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans


def main():
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 95 ms, faster than 44.79% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 13.8 MB, less than 99.90% of Python3 online submissions for Intersection of Two Arrays II.

2. Runtime: 115 ms, faster than 20.34% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 13.8 MB, less than 98.80% of Python3 online submissions for Intersection of Two Arrays II.
"""
