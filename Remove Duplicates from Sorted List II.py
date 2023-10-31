from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 더미 노드를 생성하고, 더미 노드의 다음 노드를 head로 설정합니다.
        dummy = ListNode(0)
        dummy.next = head
        # 현재 노드를 더미 노드로 초기화합니다.
        current = dummy
        
        while current.next and current.next.next:
            # 만약 현재 노드의 다음 노드와 그 다음 노드의 값이 같다면, 
            # 중복된 노드들을 찾아 제거해야 합니다.
            if current.next.val == current.next.next.val:
                # 중복된 값을 저장합니다.
                duplicate_val = current.next.val
                # 중복된 노드들을 건너뛰기 위해 while 루프를 사용합니다.
                while current.next and current.next.val == duplicate_val:
                    current.next = current.next.next
            else:
                # 만약 중복된 노드가 없다면, 현재 노드를 다음 노드로 이동합니다.
                current = current.next
                
        # 더미 노드의 다음 노드를 반환합니다.
        # 더미 노드를 사용하는 이유는 head 노드 자체가 중복되어 제거될 수 있기 때문입니다.
        return dummy.next
        