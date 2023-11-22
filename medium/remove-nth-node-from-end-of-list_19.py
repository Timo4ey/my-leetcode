# Given the head of a linked list, remove the nth node from the end
# of the list and return its head.

# Example 1:

# ￼
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]


# ---------------------------------------Runtime 45 ms Beats 80.52% Memory 16.4 MB Beats 35.23%---------------------------------------

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        node: ListNode = head
        values: list = []
        while node:
            values.append(node)
            node = node.next
        target_value: ListNode = values[-n]
        if head == target_value:
            head = head.next
            return head
        node = head
        prev = ListNode()
        while node:
            if node == target_value:
                prev.next = node.next
                break
            prev = node
            node = node.next
        return head


# Solution @scarletta
# Type Two Pointers
# Time complexity O(n)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head
