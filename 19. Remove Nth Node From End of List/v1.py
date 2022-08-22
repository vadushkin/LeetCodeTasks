class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 54 ms, faster than 45.79% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14 MB, less than 20.55% of Python3 online submissions for Remove Nth Node From End of List.

2. Runtime: 71 ms, faster than 10.16% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.8 MB, less than 98.12% of Python3 online submissions for Remove Nth Node From End of List.

3. Runtime: 44 ms, faster than 71.64% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 20.55% of Python3 online submissions for Remove Nth Node From End of List.
"""
