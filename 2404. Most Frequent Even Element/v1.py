from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        for i in Counter(nums).most_common():
            if i[0] % 2 == 0:
                return i[0]
        return -1


def main():
    s = Solution()
    print(s.mostFrequentEven([8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 829 ms
Memory Usage: 14.7 MB

2. Runtime: 733 ms
Memory Usage: 14.5 MB
"""
