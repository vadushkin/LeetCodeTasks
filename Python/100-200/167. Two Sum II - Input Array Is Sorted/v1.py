class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash_map = {}

        for i in range(len(numbers)):
            if numbers[i] in hash_map:
                return [hash_map[numbers[i]] + 1, i + 1]

            hash_map[target - numbers[i]] = i

        return []


def main():
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 125 ms Beats 91.65% 
   Memory 15.2 MB Beats 5.76%

2. Runtime 127 ms Beats 87.67% 
   Memory 15.1 MB Beats 5.76%
"""
