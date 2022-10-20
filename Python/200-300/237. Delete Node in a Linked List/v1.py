class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 77 ms, faster than 17.13% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.2 MB, less than 92.14% of Python3 online submissions for Delete Node in a Linked List.

2. Runtime: 85 ms, faster than 7.89% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.1 MB, less than 99.52% of Python3 online submissions for Delete Node in a Linked List.
"""
