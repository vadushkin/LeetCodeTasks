# Definition for singly-linked list.
from typing import Optional


# I have a high fever(
# but leetcode every day
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        b = []
        while head:
            b.append(str(head.val))
            head = head.next
        d = ''.join(b)
        if d == d[::-1]:
            return True
        return False


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 945 ms, faster than 79.03% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.8 MB, less than 29.26% of Python3 online submissions for Palindrome Linked List.

2. Runtime: 1195 ms, faster than 53.07% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 47.1 MB, less than 15.86% of Python3 online submissions for Palindrome Linked List.
"""
