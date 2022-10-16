class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1, 0, -1):
                if nums[i] == nums[j] and abs(i - j) <= k and j != i:
                    return True
        return False


def main():
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))


if __name__ == "__main__":
    main()

"""Tests:
1. TimError

2. TimError
"""
