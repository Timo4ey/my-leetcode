class Optional(list):
    ...


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# My solution 

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        repo = {}
        while head:
            next_id = id(head.next)
            cur_id = id(head)
            if not repo.get(next_id):
                repo[cur_id] = head
            else:
                return repo[next_id]
            head = head.next

        return None
