class Solution(object):

    def check(self, enum, string, summary, s):
        if enum == len(s) - 1:
            summary.append(dictionary[string])
        elif dictionary[string] < dictionary[s[enum + 1]]:
            summary.append(dictionary[s[enum + 1]] - dictionary[string])
        else:
            summary.append(dictionary[string])

    def romanToInt(self, s):
        summary = []
        if len(s) < 1 or len(s) > 15:
            return False
        for enum, string in enumerate(s):
            if string in dictionary:
                if enum != 0:
                    if dictionary[string] == dictionary[s[enum - 1]] + summary[-1]:
                        continue
                    self.check(enum, string, summary, s)
                else:
                    self.check(enum, string, summary, s)
            else:
                return False
        return sum(summary)


dictionary = {"I": 1,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 1000
              }

s = Solution()
print(s.romanToInt("III"))

"""Tests:
1. Runtime: 75 ms, faster than 29.06% of Python online submissions for Roman to Integer.
Memory Usage: 13.5 MB, less than 58.09% of Python online submissions for Roman to Integer.

2. Runtime: 64 ms, faster than 47.88% of Python online submissions for Roman to Integer.
Memory Usage: 13.3 MB, less than 82.50% of Python online submissions for Roman to Integer.
"""