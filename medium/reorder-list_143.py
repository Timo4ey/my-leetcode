# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example 1:

# ￼
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:

# ￼
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# ---------------------------------------Runtime 99 ms Beats 79.6% Memory 26 MB Beats 70.79%---------------------------------------

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_second_half(self, slow_pointer: ListNode) -> ListNode:
        second = slow_pointer.next
        prev = slow_pointer.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        return prev

    def merge_to_linked_list(self, head: ListNode, prev: ListNode) -> None:
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        self.merge_to_linked_list(head, self.reverse_second_half(slow))
