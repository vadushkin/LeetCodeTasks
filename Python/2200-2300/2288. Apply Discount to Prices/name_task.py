"""A sentence is a string of single-space separated words where each word can contain digits, lowercase letters,
and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign.

For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.
You are given a string sentence representing a sentence and an integer discount. For each word representing a price,
apply a discount of discount% on the price and update the word in the sentence.
All updated prices should be represented with exactly two decimal places.

Return a string representing the modified sentence.

Note that all prices will contain at most 10 digits.

Constraints:

1 <= sentence.length <= 105
sentence consists of lowercase English letters, digits, ' ', and '$'.
sentence does not have leading or trailing spaces.
All words in sentence are separated by a single space.
All prices will be positive numbers without leading zeros.
All prices will have at most 10 digits.
0 <= discount <= 100
"""