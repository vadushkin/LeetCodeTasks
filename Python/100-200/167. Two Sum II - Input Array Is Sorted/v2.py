class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            summary = numbers[left] + numbers[right]

            if summary == target:
                return [left + 1, right + 1]
            elif summary < target:
                left += 1
            else:
                right -= 1


def main():
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 133 ms Beats 69.70% 
   Memory 15 MB Beats 35.82%

2. Runtime 137 ms Beats 55.52% 
   Memory 14.8 MB Beats 84.72%
"""
