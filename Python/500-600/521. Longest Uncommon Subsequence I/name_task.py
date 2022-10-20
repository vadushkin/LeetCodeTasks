"""Given two strings a and b, return the length of the longest
uncommon subsequence between a and b. If the longest uncommon
subsequence does not exist, return -1.

An uncommon subsequence between two strings is a string
that is a subsequence of one but not the other.

A subsequence of a string s is a string that can be got
after deleting any amount characters from s.

For example, "abc" is a subsequence of "aebdc" because you can
delete the underlined characters in "aebdc" to get "abc".
Other subsequences of "aebdc" include "aebdc", "aeb”, and "" (empty string).

Constraints:

1 <= a.length, b.length <= 100
a and b consist of lower-case English letters.
"""
