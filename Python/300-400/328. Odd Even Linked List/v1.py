from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd, even = head, head.next
        first_even = head.next

        while even and even.next:
            temp = even.next
            even.next = even.next.next
            odd.next = temp
            temp.next = first_even
            odd = odd.next
            even = even.next

        return head


def main():
    s = Solution()
    print(s.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 80 ms Beats 62.58%
   Memory 16.6 MB Beats 78.70%

2. Runtime 93 ms Beats 37.73%
   Memory 16.6 MB Beats 78.70%
"""
