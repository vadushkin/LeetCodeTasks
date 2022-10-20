class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        return max([-abs(a), a] for a in nums)[1]

    """
    def findClosestNumber(self, nums: list[int]) -> int:
        return min(nums, key=lambda x: (abs(x), -x))

    # Tests:
    # 1. Runtime: 416 ms, faster than 8.05% of Python3 online submissions for Find Closest Number to Zero.
    #    Memory Usage: 14.1 MB, less than 91.00% of Python3 online submissions for Find Closest Number to Zero.
    # 2. Runtime: 157 ms, faster than 94.70% of Python3 online submissions for Find Closest Number to Zero.
    #    Memory Usage: 14.1 MB, less than 91.00% of Python3 online submissions for Find Closest Number to Zero.
    """

    """
    def findClosestNumber(self, nums: list[int]) -> int:
        return -min(zip(map(abs, nums), map(neg, nums)))[1]
        
    # Tests:
    # 1. Runtime: 157 ms, faster than 94.70% of Python3 online submissions for Find Closest Number to Zero.
    #    Memory Usage: 14.1 MB, less than 91.00% of Python3 online submissions for Find Closest Number to Zero.
    # 2. Runtime: 307 ms, faster than 36.65% of Python3 online submissions for Find Closest Number to Zero.
    #    Memory Usage: 14 MB, less than 91.00% of Python3 online submissions for Find Closest Number to Zero.
    """

    """
    def findClosestNumber(self, nums: list[int]) -> int:
        a = min(map(abs, nums))
        return a if a in nums else -a
    
    # Tests:
    # 1. Runtime: 340 ms, faster than 25.00% of Python3 online submissions for Find Closest Number to Zero.
    #    Memory Usage: 14.1 MB, less than 91.00% of Python3 online submissions for Find Closest Number to Zero.
    # 2. Runtime: 337 ms, faster than 25.85% of Python3 online submissions for Find Closest Number to Zero.
    #    Memory Usage: 14.2 MB, less than 48.20% of Python3 online submissions for Find Closest Number to Zero.
    """


def main():
    s = Solution()
    print(s.findClosestNumber([-4, -2, -1, 0, 1, 4, 8]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 335 ms, faster than 26.99% of Python3 online submissions for Find Closest Number to Zero.
Memory Usage: 14.2 MB, less than 48.20% of Python3 online submissions for Find Closest Number to Zero.

2. Runtime: 372 ms, faster than 15.91% of Python3 online submissions for Find Closest Number to Zero.
Memory Usage: 14 MB, less than 91.00% of Python3 online submissions for Find Closest Number to Zero.
"""
