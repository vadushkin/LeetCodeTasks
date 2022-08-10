class Solution:
    def plusOne(self, digits):
        digits = int(''.join([str(i) for i in digits]))
        digits += 1
        res = list(str(digits))
        res = [int(i) for i in res]
        return res


s = Solution()
print(s.plusOne([1, 2, 3, 4]))


"""Tests:
1. Runtime: 79 ms, faster than 5.47% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 58.70% of Python3 online submissions for Plus One.

2. Runtime: 53 ms, faster than 46.14% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 11.85% of Python3 online submissions for Plus One.

3. Runtime: 39 ms, faster than 82.63% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 11.85% of Python3 online submissions for Plus One.
"""