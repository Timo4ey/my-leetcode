# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.


# Example 1:

# ￼
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:

# ￼
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# ---------------------------------------Runtime 56 ms Beats 63.92% Memory 16.4 MB Beats 13.36%---------------------------------------

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity O(n)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack: set = set()
        node: ListNode = head
        while node:
            if node.val not in stack:
                stack.add(node.val)
            else:
                prev.next = node.next
                node = prev
            prev = node
            node = node.next
        return head
