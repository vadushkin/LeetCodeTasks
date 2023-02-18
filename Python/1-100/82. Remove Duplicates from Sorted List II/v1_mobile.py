class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        dummy.next = head

        fast, slow = head, dummy

        while fast:

            while fast.next and fast.val == fast.next.val:

                fast = fast.next

            if slow.next == fast:

                slow, fast = slow.next, fast.next

            else:

                slow.next = fast.next

                fast = slow.next

                

        return dummy.next
