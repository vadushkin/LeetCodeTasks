from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return

        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next

        slow.next = None

        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root


def main():
    s = Solution()
    print(s.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 124 ms Beats 71.79% 
   Memory 20.3 MB Beats 49.5%

2. Runtime 117 ms Beats 92.31% 
   Memory 17.8 MB Beats 76.92%
"""
