class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:

            return head

        middle_node = self.find_middle_node(head)

        right_head = middle_node.next

        middle_node.next = None

        return self.merge(self.sortList(head), self.sortList(right_head))

    

    def find_middle_node(self, head):

        slow, fast = head, head

        while fast and fast.next and fast.next.next:

            fast = fast.next.next

            slow = slow.next

        return slow

        

    def merge(self, head1, head2):

        dummy = ListNode(None)

        node = dummy

        while head1 and head2:

            if head1.val < head2.val:

                node.next = head1

                head1 = head1.next

            else:

                node.next = head2

                head2 = head2.next

            node = node.next

            

        node.next = head1 or head2

        return dummy.next
