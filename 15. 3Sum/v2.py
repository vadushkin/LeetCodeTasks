from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if not (3 <= len(nums) <= 3000):
#             return []
#         result = []
#         for i in range(0, len(nums) - 1):
#             for j in range(i + 1, len(nums) - 1):
#                 for s in range(j + 1, len(nums)):
#                     if not (-100000 <= nums[i] <= 100000):
#                         return []
#                     if nums[i] + nums[j] + nums[s] == 0:
#                         sort_list = sorted([nums[i], nums[j], nums[s]])
#                         if not (sort_list in result):
#                             result.append(sort_list)
#
#         return result
# time error

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))
        if len(z) >= 3:
            res.add((0, 0, 0))
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))
        return res


s = Solution()
print(s.threeSum([1, 2, -1, -2, 0]))


"""Tests:
1. Runtime: 1021 ms, faster than 73.70% of Python3 online submissions for 3Sum.
Memory Usage: 18.5 MB, less than 13.23% of Python3 online submissions for 3Sum.

2. Runtime: 887 ms, faster than 82.75% of Python3 online submissions for 3Sum.
Memory Usage: 18.5 MB, less than 13.23% of Python3 online submissions for 3Sum.

3. Runtime: 800 ms, faster than 88.51% of Python3 online submissions for 3Sum.
Memory Usage: 18.6 MB, less than 13.23% of Python3 online submissions for 3Sum.
"""
