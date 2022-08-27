class Solution:
    def deleteNode(self, node):
        cur = node
        while node.next != None:
            node.val = node.next.val
            cur = node
            node = node.next
        cur.next = None


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 67 ms, faster than 37.94% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.1 MB, less than 92.14% of Python3 online submissions for Delete Node in a Linked List.

2. Runtime: 58 ms, faster than 59.38% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.2 MB, less than 54.84% of Python3 online submissions for Delete Node in a Linked List.
"""
