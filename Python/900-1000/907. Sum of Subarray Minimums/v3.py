class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        dp = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                previous_smaller = stack[-1]
                dp[i] = dp[previous_smaller] + (i - previous_smaller) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]

            stack.append(i)

        return sum(dp) % MOD


def main():
    s = Solution()
    print(s.sumSubarrayMins([3, 1, 2, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 474 ms Beats 94.59%
   Memory 18.9 MB Beats 34.26%

2. Runtime 1433 ms Beats 23.18%
   Memory 18.8 MB Beats 83.15%
"""
