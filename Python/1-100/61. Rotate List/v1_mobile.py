class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        last, n = head, 1
        while last.next:
            last = last.next
            n += 1
            
        if k % n == 0: return head
        
        middle = head
        for i in range(n - k%n-1):
            middle = middle.next
            
        new_head = middle.next
        last.next = head
        middle.next = None
        return new_head
