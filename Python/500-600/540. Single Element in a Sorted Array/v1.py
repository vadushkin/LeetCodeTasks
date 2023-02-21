class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        ans = 0
        is_neg = False

        for i in range(32):
            counter = 0

            for num in nums:
                if (num >> i) & 1:
                    counter += 1

            if counter % 2 == 1:
                ans += pow(2, i)

                if i == 31:
                    is_neg = True

        return ans if not is_neg else ans - pow(2, 32)


def main():
    s = Solution()
    print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 462 ms Beats 5.2% 
   Memory 23.6 MB Beats 86.81%

2. Runtime 494 ms Beats 5.2% 
   Memory 23.7 MB Beats 86.81%
"""
