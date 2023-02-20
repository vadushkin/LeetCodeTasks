class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)

        dummyHead.next = nodeToInsert = head

        

        while head and head.next:

            if head.val > head.next.val:


                nodeToInsert = head.next


                nodeToInsertPre = dummyHead

                while nodeToInsertPre.next.val < nodeToInsert.val:

                    nodeToInsertPre = nodeToInsertPre.next

                    

                head.next = nodeToInsert.next


                nodeToInsert.next = nodeToInsertPre.next

                nodeToInsertPre.next = nodeToInsert

            else:

                head = head.next

            

        return dummyHead.next
