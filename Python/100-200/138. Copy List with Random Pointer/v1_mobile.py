class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    
    if not head:
        return None
    

    visited={}
    cur=head
    while cur:
        visited[cur]=Node(cur.val, None, None)
        cur=cur.next
    
    cur=head
    while cur:
        if cur.random:
            visited[cur].random=visited[cur.random]
        if cur.next:
            visited[cur].next=visited[cur.next]
        cur=cur.next
    
    return visited[head]
