class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.remove(head, n)[1]

    def remove(self, head, n):
        if not head:
            return 0, head

        i, head.next = self.remove(head.next, n)

        return i + 1, (head, head.next)[i + 1 == n]


def main():
    s = Solution()
    print(s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 35 ms Beats 69.30% 
   Memory 13.9 MB Beats 62.7%
 
2. Runtime 27 ms Beats 96.62% 
   Memory 14 MB Beats 14.26%
"""
