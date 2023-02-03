class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        right = []
        number_of_zeros = 0

        for i in range(len(nums)):
            if nums[i] == float("infinity"):
                continue

            if i == len(nums) - 1:
                if nums[i] == 0:
                    number_of_zeros += 1
                else:
                    right.append(nums[i])
                break

            if nums[i] == 0:
                number_of_zeros += 1

            elif nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = float("infinity")

                number_of_zeros += 1
                right.append(nums[i])
            else:
                right.append(nums[i])

        return right + [0] * number_of_zeros


def main():
    s = Solution()
    print(s.applyOperations([0, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 58 ms Beats 59.11% 
   Memory 14.2 MB Beats 54.21%

2. Runtime 54 ms Beats 75.4% 
   Memory 14.2 MB Beats 54.21%
"""
