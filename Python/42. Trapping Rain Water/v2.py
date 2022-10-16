class Solution:
    def trap(self, height: list[int]) -> int:

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water


def main():
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 270 ms, faster than 24.72% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 15.9 MB, less than 81.24% of Python3 online submissions for Trapping Rain Water.

2. Runtime: 249 ms, faster than 33.21% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16 MB, less than 81.24% of Python3 online submissions for Trapping Rain Water.

3. Runtime: 271 ms, faster than 24.41% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 16.1 MB, less than 44.51% of Python3 online submissions for Trapping Rain Water.
"""
