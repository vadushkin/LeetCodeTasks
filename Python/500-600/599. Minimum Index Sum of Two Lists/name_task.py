"""Given two arrays of strings list1 and list2,
find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string
such that if it appeared at list1[i] and list2[j] then i + j
should be the minimum value among all the other common strings.

Return all the common strings with the least index sum.
Return the answer in any order.

Constraints:

1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the strings of list1 are unique.
All the strings of list2 are unique.
"""
