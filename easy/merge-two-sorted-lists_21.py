# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:

# ￼
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# My solution
### Notes i tried to solve this task user a recursion approach


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            new_list = list2
            return new_list
        if list2 is None:
            new_list = list1
            return new_list

        def new_node(
            list1: Optional[ListNode], list2: Optional[ListNode]
        ) -> Optional[ListNode]:
            new_list = ListNode()
            if (
                list1 is not None and list2 is not None
            ) and list1.val <= list2.val:
                new_list.val = list1.val
                new_list.next = new_node(list1.next, list2)

            elif (
                list1 is not None and list2 is not None
            ) and list1.val > list2.val:
                new_list.val = list2.val
                new_list.next = new_node(list1, list2.next)

            elif (list1 is not None and list2 is None) and list1.next is None:
                return ListNode(list1.val)
            elif (list2 is not None and list1 is None) and list2.next is None:
                return ListNode(list2.val)

            elif list1 is not None and list2 is None:
                new_list.val = list1.val
                new_list.next = new_node(list1.next, list2)
            elif list2 is not None and list1 is None:
                new_list.val = list2.val
                new_list.next = new_node(list1, list2.next)

            return new_list

        return new_node(list1, list2)


# Approach artod
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
