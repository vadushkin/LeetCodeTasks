class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        possible_dups = 0
        length = len(arr) - 1

        for left in range(length + 1):
            if left > length - possible_dups:
                break

            if arr[left] == 0:
                if left == length - possible_dups:
                    arr[length] = 0
                    length -= 1
                    break

                possible_dups += 1

        last = length - possible_dups

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]


def main():
    s = Solution()
    print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 73 ms Beats 74.33%
   Memory 14.9 MB Beats 63.24%

2. Runtime 61 ms Beats 98.40%
   Memory 14.9 MB Beats 22.23%
"""
