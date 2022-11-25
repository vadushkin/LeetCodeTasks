class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:

        total_sum = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                total_sum += min(arr[i:j])

        return total_sum


def main():
    s = Solution()
    print(s.sumSubarrayMins([3, 1, 2, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Time Limit Exceeded
   71 / 87 testcases passed

2. Time Limit Exceeded 
   69 / 87 testcases passed
   
3. Time Limit Exceeded
   72 / 87 testcases passed
"""
