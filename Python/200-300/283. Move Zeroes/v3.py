class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        number_of_zeros = 0
        numbers = []

        for i in nums:
            if i:
                numbers.append(i)
            else:
                number_of_zeros += 1

        nums[:] = numbers + [0] * number_of_zeros


def main():
    s = Solution()
    print(s.moveZeroes([0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 3, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 165 ms Beats 89.6% 
   Memory 15.6 MB Beats 56.19%
   
2. Runtime 159 ms Beats 96.62% 
   Memory 15.5 MB Beats 56.19%
"""
