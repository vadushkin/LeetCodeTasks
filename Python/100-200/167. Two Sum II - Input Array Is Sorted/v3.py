class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]

            while left <= right:
                mid = left + (right - left) // 2

                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1


def main():
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 222 ms Beats 22.35% 
   Memory 14.9 MB Beats 84.72%

2. Runtime 222 ms Beats 22.35% 
   Memory 14.9 MB Beats 84.72%
"""
