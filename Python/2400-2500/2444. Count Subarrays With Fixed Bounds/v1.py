class Solution:
    def countSubarrays(self, nums: list[int], min_k: int, max_k: int) -> int:
        res = 0
        j_min = j_max = j_bad = -1

        for i, num in enumerate(nums):
            if not min_k <= num <= max_k:
                j_bad = i

            if num == min_k:
                j_min = i

            if num == max_k:
                j_max = i

            res += max(0, min(j_min, j_max) - j_bad)

        return res


def main():
    s = Solution()
    print(s.countSubarrays([1, 1, 1, 1], 1, 1))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 876 ms Beats 81.67% 
   Memory 28.6 MB Beats 69.78%

2. Runtime 890 ms Beats 71.71% 
   Memory 28.5 MB Beats 85.53%
"""
