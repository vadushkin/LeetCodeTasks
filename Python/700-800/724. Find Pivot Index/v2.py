class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[:i:]) == sum(nums[i + 1::]):
                return i

        return -1


def main():
    s = Solution()
    print(s.pivotIndex([1, 7, 3, 6, 5, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. 741 / 745 testcases passed

2. 742 / 745 testcases passed

3. Runtime 8752 ms Beats 5.1%
   Memory 15.1 MB Beats 92.61%
"""
