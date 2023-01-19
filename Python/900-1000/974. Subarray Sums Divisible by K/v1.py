class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # bruteforce
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if not sum(nums[i:j]) % k:
                    count += 1

        return count


def main():
    s = Solution()
    print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Time Limit Exceeded
   38 / 73 testcases passed

2. Time Limit Exceeded
   38 / 73 testcases passed
"""
