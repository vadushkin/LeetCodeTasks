class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = []

        for i, j in zip(nums[:n], nums[n:]):
            res += [i, j]

        return res


def main():
    s = Solution()
    print(s.shuffle([2, 5, 1, 3, 4, 7], 3))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 64 ms Beats 66.70% 
   Memory 14.2 MB Beats 33.52%

2. Runtime 63 ms Beats 70.68% 
   Memory 14.2 MB Beats 33.52%
"""
