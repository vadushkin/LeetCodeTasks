class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            result = 0
            for n in num:  # for... O_O
                result = result * 10 + ord(n) - ord('0')
            return result

        return str(str2int(num1) + str2int(num2))


s = Solution()
print(s.addStrings('23', '123'))

"""Tests:
1. Runtime: 88 ms, faster than 22.05% of Python3 online submissions for Add Strings.
Memory Usage: 14 MB, less than 62.00% of Python3 online submissions for Add Strings

2. Runtime: 63 ms, faster than 54.95% of Python3 online submissions for Add Strings.
Memory Usage: 13.9 MB, less than 89.68% of Python3 online submissions for Add Strings.

3. Runtime: 74 ms, faster than 37.90% of Python3 online submissions for Add Strings.
Memory Usage: 13.9 MB, less than 62.00% of Python3 online submissions for Add Strings.
"""