class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        K = 10000
        element_to_count = [0] * (2 * K + 1)

        for element in nums:
            element_to_count[element + K] += 1

        max_sum = 0
        is_even_index = True

        for element in range(2 * K + 1):
            while element_to_count[element] > 0:
                if is_even_index:
                    max_sum += element - K

                is_even_index = not is_even_index
                element_to_count[element] -= 1

        return max_sum


def main():
    s = Solution()
    print(s.arrayPairSum([1, 4, 2, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1102 ms Beats 5.2%
   Memory 16.6 MB Beats 81.31%

2. Runtime 1012 ms Beats 5.2%
   Memory 16.7 MB Beats 56.64%
"""
