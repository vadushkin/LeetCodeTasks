from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                tmp = curr.next
                curr.next = curr.next.next
                del tmp
            else:
                curr = curr.next
        return head


def main():
    s = Solution()
    print(s.deleteDuplicates(ListNode(val=1, next=ListNode(val=1, next=ListNode(val=1, next=None)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 80 ms, faster than 26.79% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14 MB, less than 30.08% of Python3 online submissions for Remove Duplicates from Sorted List.

2. Runtime: 54 ms, faster than 75.57% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.8 MB, less than 72.40% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
