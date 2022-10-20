class Solution():
    # genius
    def removeNthFromEnd(self, head, n):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        stack.pop(len(stack) - n)

        out, prev = None, None
        while stack:
            out = stack.pop()
            out.next = prev
            prev = out
        return out


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 38 ms, faster than 86.01% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.8 MB, less than 70.57% of Python3 online submissions for Remove Nth Node From End of List.

2. Runtime: 32 ms, faster than 96.40% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 20.55% of Python3 online submissions for Remove Nth Node From End of List.
"""
