class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        hash_map = {
            arr2_value: index
            for index, arr2_value in enumerate(arr2)
        }
        return sorted(arr1, key=lambda arr1_value: hash_map.get(arr1_value, 1000 + arr1_value))


def main():
    s = Solution()
    print(s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 46 ms Beats 44.2%  
   Memory 14 MB Beats 32.53%

2. Runtime 47 ms Beats 40.27%  
   Memory 13.9 MB Beats 68.41% 
"""
