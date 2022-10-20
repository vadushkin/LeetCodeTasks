# Такая же реализация только без словаря
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        count = 0
        direction = 1
        final = [''] * numRows

        for string in s:
            final[count] += string

            if count == numRows - 1:
                direction = -1
            if count == 0:
                direction = 1
            count += direction
        return "".join(final)


s = Solution()
print(s.convert("amongussss", 4))

"""Tests:
1.  Runtime: 64 ms, faster than 89.07% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 13.9 MB, less than 95.77% of Python3 online submissions for Zigzag Conversion.

2. Runtime: 87 ms, faster than 64.52% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 13.9 MB, less than 75.51% of Python3 online submissions for Zigzag Conversion.
"""
