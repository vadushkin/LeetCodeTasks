class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# forward backward tactics
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 738 ms, faster than 97.94% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 39.3 MB, less than 65.33% of Python3 online submissions for Palindrome Linked List.

2. Runtime: 1204 ms, faster than 52.03% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 39.2 MB, less than 65.33% of Python3 online submissions for Palindrome Linked List.
"""
