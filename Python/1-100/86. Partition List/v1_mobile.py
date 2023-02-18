class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        fdum, bdum = ListNode(0), ListNode(0)

        front, back, curr = fdum, bdum, head

        while curr:

            if curr.val < x:

                front.next = curr

                front = curr

            else:

                back.next = curr

                back = curr

            curr = curr.next

        front.next, back.next = bdum.next, None

        return fdum.next
