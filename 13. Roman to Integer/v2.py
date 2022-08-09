class Solution(object):
    def romanToInt(self, s):
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            total = total + ((-1) ** (dict[s[i]] < dict[s[i + 1]])) * dict[s[i]]
        return total + dictionary[s[len(s) - 1]]
