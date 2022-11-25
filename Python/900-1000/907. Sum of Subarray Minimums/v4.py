class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        mod = 10 ** 9 + 7
        total_sum = 0

        stack = []
        arr = [float('-inf')] + arr + [float('-inf')]

        for index, element in enumerate(arr):
            while stack and arr[stack[-1]] > element:
                current = stack.pop()
                total_sum += arr[current] * (index - current) * (current - stack[-1])
            stack.append(index)

        return total_sum % mod


def main():
    s = Solution()
    print(s.sumSubarrayMins([3, 1, 4, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1180 ms Beats 50.92%
   Memory 18.9 MB Beats 34.26%

2. Runtime 661 ms Beats 76.57%
   Memory 18.8 MB Beats 60.96%
"""
