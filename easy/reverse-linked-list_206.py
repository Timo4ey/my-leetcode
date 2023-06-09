# task https://leetcode.com/problems/reverse-linked-list/


class Optional(list):
    ...


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# My solution


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        values.reverse()
        obj = ListNode(values[0])
        head_obj = obj
        for i in range(1, len(values)):
            new_obj = ListNode(values[i])
            obj.next = new_obj
            obj = new_obj

        return head_obj


# Solution Neetcode . Recursion


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T O(n), M O(n)

        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head


# Solution PratikSen07


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize prev pointer as NULL...
        prev = None
        # Initialize the curr pointer as the head...
        curr = head
        # Run a loop till curr points to NULL...
        while curr:
            # Initialize next pointer as the next pointer of curr...
            next = curr.next
            # Now assign the prev pointer to curr’s next pointer.
            curr.next = prev
            # Assign curr to prev, next to curr...
            prev = curr
            curr = next
        return (
            prev  # Return the prev pointer to get the reverse linked list...
        )
