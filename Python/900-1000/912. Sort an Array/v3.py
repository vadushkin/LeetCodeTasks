class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # self.quickSort(nums)
        # self.mergeSort(nums)
        self.bubbleSort(nums)
        # self.insertionSort(nums)
        # self.selectionSort(nums)
        # self.heapSort(nums)
        return nums

    def bubbleSort(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    def selectionSort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            _min = min(nums[i:])
            min_index = nums[i:].index(_min)
            nums[i + min_index] = nums[i]
            nums[i] = _min

        return nums

    def quickSort(self, nums: list[int]) -> list[int]:
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

    def mergeSort(self, nums: list[int]) -> None:
        if len(nums) > 1:
            mid = len(nums) // 2

            left = nums[:mid]
            right = nums[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

    def heapSort(self, nums: list[int]) -> None:
        def heapify(nums_: list[int], n_: int, i_: int) -> None:
            left = 2 * i_ + 1
            right = 2 * i_ + 2

            largest = i_

            if left < n_ and nums_[largest] < nums_[left]:
                largest = left

            if right < n_ and nums_[largest] < nums_[right]:
                largest = right

            if largest != i_:
                nums_[i_], nums_[largest] = nums_[largest], nums_[i_]
                heapify(nums_, n_, largest)

        n = len(nums)

        for i in range(n // 2 + 1)[::-1]:
            heapify(nums, n, i)

        for i in range(n)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. 

2. 
"""
