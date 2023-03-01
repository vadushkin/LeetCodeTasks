class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.quick_sort(nums)

        return nums

    @staticmethod
    def quick_sort(nums: list[int]) -> list[int]:
        def helper(head: int, tail: int) -> None:
            if head >= tail:
                return

            left, right = head, tail
            middle = (right - left) // 2 + left

            pivot = nums[middle]

            while right >= left:
                while right >= left and nums[left] < pivot:
                    left += 1

                while right >= left and nums[right] > pivot:
                    right -= 1

                if right >= left:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

            helper(head, right)
            helper(left, tail)

        helper(0, len(nums) - 1)
        return nums


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. TLE

2. TLE
"""
