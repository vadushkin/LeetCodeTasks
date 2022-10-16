from collections import Counter


class Solution:
    def findOriginalArray(self, nums: list[int]) -> list[int]:
        ans = []
        if len(nums) % 2:
            return ans
        nums.sort()
        temp = Counter(nums)
        for i in nums:
            if temp[i] == 0:
                continue
            else:
                if temp.get(2 * i, 0) >= 1:
                    ans.append(i)
                    temp[2 * i] -= 1
                    temp[i] -= 1
                else:
                    return []
        return ans


def main():
    s = Solution()
    print(s.findOriginalArray([1, 2, 3, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2507 ms, faster than 38.37% of Python3 online submissions for Find Original Array From Doubled Array.
Memory Usage: 32.8 MB, less than 49.63% of Python3 online submissions for Find Original Array From Doubled Array.

2. Runtime: 3283 ms, faster than 13.33% of Python3 online submissions for Find Original Array From Doubled Array.
Memory Usage: 32.8 MB, less than 49.63% of Python3 online submissions for Find Original Array From Doubled Array.
"""
