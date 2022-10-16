class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head.next = self.reverseKGroup(curr, k)
        return prev


def main():
    s = Solution()
    # print(s.reverseKGroup())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 110 ms, faster than 7.76% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.2 MB, less than 40.32% of Python3 online submissions for Reverse Nodes in k-Group.

2. Runtime: 66 ms, faster than 69.77% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.3 MB, less than 40.32% of Python3 online submissions for Reverse Nodes in k-Group.

3. Runtime: 95 ms, faster than 20.26% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.3 MB, less than 40.32% of Python3 online submissions for Reverse Nodes in k-Group.
"""
