class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


def main():
    s = Solution()
    print(s.set_intersection([1, 2, 3], [2, 3, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 84 ms, faster than 43.99% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.1 MB, less than 68.57% of Python3 online submissions for Intersection of Two Arrays.

2. Runtime: 97 ms, faster than 26.22% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.1 MB, less than 25.09% of Python3 online submissions for Intersection of Two Arrays.
"""
