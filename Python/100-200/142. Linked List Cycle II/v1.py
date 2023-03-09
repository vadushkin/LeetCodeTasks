from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                break
        else:
            return None

        while head != slow:
            head, slow = head.next, slow.next

        return head


def main():
    s = Solution()
    print(s.detectCycle(ListNode(3, ListNode(2, ListNode(0, ListNode(4))))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 58 ms Beats 35.44% 
   Memory 17.4 MB Beats 31.92%

2. Runtime 53 ms Beats 63.17% 
   Memory 17.3 MB Beats 90.55%
"""
