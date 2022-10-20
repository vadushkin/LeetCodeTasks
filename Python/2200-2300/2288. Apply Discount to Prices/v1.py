class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        split_sentence = sentence.split()
        difference = discount / 100
        for e, word in enumerate(split_sentence):
            if word[0] == "$" and word[1:].isdigit():
                num = int(word[1:]) * (1 - difference)
                string = "$" + "{:.2f}".format(num)
                split_sentence[e] = string

        return " ".join(split_sentence)


s = Solution()
print(s.discountPrices("there are $1 $2 and 5$ candies in the shop", 20))

"""Tests:
1. Runtime: 114 ms, faster than 98.60% of Python3 online submissions for Apply Discount to Prices.
Memory Usage: 16 MB, less than 88.77% of Python3 online submissions for Apply Discount to Prices.

2. Runtime: 149 ms, faster than 85.64% of Python3 online submissions for Apply Discount to Prices.
Memory Usage: 16 MB, less than 63.93% of Python3 online submissions for Apply Discount to Prices.
"""
