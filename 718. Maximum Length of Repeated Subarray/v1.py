class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        str_num2 = ''.join([chr(x) for x in nums2])
        str_max = ''
        ans = 0
        for num in nums1:
            str_max += chr(num)
            if str_max in str_num2:
                ans = max(ans, len(str_max))
            else:
                str_max = str_max[1:]
        return ans


def main():
    s = Solution()
    print(s.findLength([5, 6, 7, 8, 1], [0, 1, 2, 3, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 256 ms, faster than 96.74% of Python3 online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 14 MB, less than 88.72% of Python3 online submissions for Maximum Length of Repeated Subarray.

2. Runtime: 141 ms, faster than 99.96% of Python3 online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 14 MB, less than 94.69% of Python3 online submissions for Maximum Length of Repeated Subarray.
"""
