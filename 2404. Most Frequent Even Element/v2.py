class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        freq = -1
        ans = -1
        for i in sorted(set(nums)):
            if i % 2 == 0 and nums.count(i) > freq:
                freq = nums.count(i)
                ans = i
        return ans


def main():
    s = Solution()
    print(s.mostFrequentEven([8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4369 ms, faster than 10.00% of Python3 online submissions for Most Frequent Even Element.
Memory Usage: 14.4 MB, less than 20.00% of Python3 online submissions for Most Frequent Even Element.

2. Runtime: 1688 ms, faster than 10.00% of Python3 online submissions for Most Frequent Even Element.
Memory Usage: 14.4 MB, less than 20.00% of Python3 online submissions for Most Frequent Even Element.
"""
