class Solution:
    def myAtoi(self, s: str) -> int:
        if s is None or len(s) < 1:
            return 0

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        s = s.lstrip()
        i = 0

        isNegative = len(s) > 1 and s[0] == '-'
        isPositive = len(s) > 1 and s[0] == '+'

        if isNegative:
            i += 1
        elif isPositive:
            i += 1

        number = 0

        while i < len(s) and '0' <= s[i] <= '9':
            number = number * 10 + (ord(s[i]) - ord('0'))
            i += 1
        if isNegative:
            number = -number
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX
        return number


s = Solution()
print(s.myAtoi("          +314159 wqwer"))

"""Tests:
1. Runtime: 39 ms, faster than 89.23% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 79.66% of Python3 online submissions for String to Integer (atoi).

2. Runtime: 65 ms, faster than 28.48% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14 MB, less than 29.23% of Python3 online submissions for String to Integer (atoi).

3. Runtime: 52 ms, faster than 59.53% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.8 MB, less than 79.66% of Python3 online submissions for String to Integer (atoi).

4. Runtime: 43 ms, faster than 80.60% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 79.66% of Python3 online submissions for String to Integer (atoi).
"""