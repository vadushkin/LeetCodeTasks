class Solution:
    def myAtoi(self, s: str) -> int:

        string = ""
        sign = ""
        s = s.strip()

        for e, i in enumerate(s):
            if not string and (i == '-' or i == '+'):
                if sign:
                    return 0
                sign = i
                continue
            try:
                int(i)
                string += i
            except:
                break

        if not string:
            return 0

        if int(sign + string) > 2147483647:
            return 2147483647
        if int(sign + string) < -2147483648:
            return -2147483648

        return int(sign + string)


s = Solution()
print(s.myAtoi("          +314159 wqwer"))

"""Tests:
1. Runtime: 48 ms, faster than 68.95% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 79.66% of Python3 online submissions for String to Integer (atoi).

2. Runtime: 67 ms, faster than 24.39% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 79.66% of Python3 online submissions for String to Integer (atoi).

3. Runtime: 54 ms, faster than 54.55% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14 MB, less than 29.23% of Python3 online submissions for String to Integer (atoi).

4. Runtime: 44 ms, faster than 78.22% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 79.66% of Python3 online submissions for String to Integer (atoi).
"""