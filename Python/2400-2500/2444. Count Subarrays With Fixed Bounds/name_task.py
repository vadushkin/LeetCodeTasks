"""
You are given an integer array nums and two integers
A fixed-bound subarray of nums is a subarray that satisfies

* Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

* Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Constraints:

* minK
* maxK
* 2 <= nums.length <= 105
* 1 <= nums[i], minK, maxK <= 106
"""