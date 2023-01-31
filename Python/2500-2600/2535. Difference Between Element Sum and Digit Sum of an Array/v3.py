class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        return sum(nums) - sum((int(j) for i in nums for j in str(i)))


def main():
    s = Solution()
    print(s.differenceOfSum([1, 15, 6, 3]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 152 ms Beats 44.69% 
   Memory 14.2 MB Beats 17.2%
   
2. Runtime 147 ms Beats 55.11% 
   Memory 14.1 MB Beats 52.47%
"""
