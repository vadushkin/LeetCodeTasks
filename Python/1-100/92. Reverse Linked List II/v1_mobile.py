class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:

            return head

        

        dummy_head = ListNode(val=-1, next=head)

        p_prev = dummy_head

        


        for _ in range(left - 1):

            p_prev = p_prev.next

            

        p_cur = p_prev.next

        


        for _ in range(right - left):

            p_next = p_cur.next

            p_cur.next = p_next.next

            p_next.next = p_prev.next

            p_prev.next = p_next

        

        return dummy_head.next
