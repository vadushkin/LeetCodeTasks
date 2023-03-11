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
    def __init__(self):
        self.arr = None

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.arr = self.convertToArray(head)
        return self.dfs(0, len(self.arr) - 1)

    def convertToArray(self, head):
        arr = []

        while head is not None:
            arr.append(head.val)
            head = head.next

        return arr

    def dfs(self, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2

        root = TreeNode(self.arr[mid])

        root.left = self.dfs(left, mid - 1)
        root.right = self.dfs(mid + 1, right)

        return root


def main():
    s = Solution()
    print(s.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 124 ms Beats 71.79% 
   Memory 20.3 MB Beats 49.5%

2. Runtime 123 ms Beats 75.77% 
   Memory 20.3 MB Beats 49.5%
"""
