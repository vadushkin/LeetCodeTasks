class Solution:
    def addToArrayForm(self, A, K):
        for i in range(len(A) - 1, -1, -1):
            K, A[i] = divmod(A[i] + K, 10)
        return [int(i) for i in str(K)] + A if K else A


s = Solution()
print(s.addToArrayForm([1], 1))

"""Tests:
1. Runtime: 369 ms, faster than 74.79% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.1 MB, less than 51.67% of Python3 online submissions for Add to Array-Form of Integer.

2. Runtime: 468 ms, faster than 48.21% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.1 MB, less than 27.46% of Python3 online submissions for Add to Array-Form of Integer.

3. Runtime: 556 ms, faster than 29.12% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15 MB, less than 51.67% of Python3 online submissions for Add to Array-Form of Integer.
"""
