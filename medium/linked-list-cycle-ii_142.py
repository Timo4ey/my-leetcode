# iven the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.


# Example 1:

# ￼
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:

# ￼
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:

# ￼
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


# Definition for singly-linked list.
# ---------------------------------------Runtime 53 ms Beats 53.19% Memory 17.6 MB  Beats 100%---------------------------------------

from typing import Optional


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
