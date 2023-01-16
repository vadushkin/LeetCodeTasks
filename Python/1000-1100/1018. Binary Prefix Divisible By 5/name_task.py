"""You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is
the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""