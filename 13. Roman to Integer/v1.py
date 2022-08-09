class Solution(object):

    def check(self, enum, string, summary, s):
        if enum == len(s) - 1:
            summary.append(dictionary[string])
        elif dictionary[string] < dictionary[s[enum + 1]]:
            summary.append(dictionary[s[enum + 1]] - dictionary[string])
        else:
            summary.append(dictionary[string])

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
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

        print(summary)
        return sum(summary)


dictionary = {"I": 1,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 1000
              }
