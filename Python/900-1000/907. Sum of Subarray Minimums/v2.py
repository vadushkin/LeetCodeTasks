class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        sum_of_minimums = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i

                count = (mid - left_boundary) * (right_boundary - mid)
                sum_of_minimums += (count * arr[mid])

            stack.append(i)

        return sum_of_minimums % MOD


def main():
    s = Solution()
    print(s.sumSubarrayMins([3, 1, 2, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1537 ms Beats 16.25%
   Memory 18.4 MB Beats 98.89%

2. Runtime 1170 ms Beats 51.96%
   Memory 18.7 MB Beats 94.38%
"""
