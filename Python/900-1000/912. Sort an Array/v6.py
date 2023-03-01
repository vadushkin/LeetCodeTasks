class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.heap_sort(nums)
        return nums

    @staticmethod
    def heap_sort(nums: list[int]) -> None:
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
1. Runtime 2635 ms Beats 19.51% 
   Memory 21.2 MB Beats 99.38%

2. Runtime 2622 ms Beats 19.82% 
   Memory 21.2 MB Beats 99.38%
"""
