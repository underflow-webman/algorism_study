from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy=ListNode(-1)
        dummy.next=head
        
        back=dummy
        front=dummy
        
        for i in range(n): #Move front cursor by 'n'
            front=front.next
            
        while front.next!=None: # Move front, back cursor by 1 until next node of front is null
            front=front.next
            back=back.next
        
        back.next=back.next.next # Remove target and link back node with next node of target
        
        return dummy.next