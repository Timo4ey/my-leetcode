# Given the head of a linked list and an integer val, remove all the nodes
# of the linked list that has Node.val == val, and return the new head.


# Example 1:

# ￼
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

# ---------------------------------------Runtime 65 ms Beats 99.56% Memory 19.9 MB Beats 48.82%---------------------------------------

# Time complexity O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        while True:
            if head and head.val == val:
                head = head.next
            else:
                node: ListNode = head
                prev = node
                while node:
                    if node.val == val:
                        prev.next = node.next
                        node = prev
                    prev = node
                    node = node.next
                if node is None:
                    return head
