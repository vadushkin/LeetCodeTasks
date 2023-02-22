class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result = []
        dictionary = dict()

        for key, value in nums1:
            dictionary[key] = value

        for key, value in nums2:
            dictionary[key] = dictionary.get(key, 0) + value

        for key, value in dictionary.items():
            result.append([key, value])

        return sorted(result)


def main():
    s = Solution()
    print(s.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 69 ms Beats 34.8% 
   Memory 14.1 MB Beats 80.50%

2. Runtime 70 ms Beats 30.21% 
   Memory 14.1 MB Beats 80.50%
"""
