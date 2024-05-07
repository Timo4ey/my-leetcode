# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.

# Example 1:

# ￼
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
# Example 2:

# ￼
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.


# Constraints:

# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

# ---------------------------------------Runtime 367 ms Beats 22.38% Memory 20.01 MB Beats 40.22%---------------------------------------


import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(50000)
        num = ""

        while head:
            num = f"{num}{head.val}"
            head = head.next

        num = str(int(num) * 2)

        head = node = None
        for i in num:
            if not head:
                head = ListNode(i)
                node = head
            else:
                node.next = ListNode(i)
                node = node.next
        return head


# Solution 2
# ---------------------------------------Runtime 288 ms Beats 42.41% Memory 20.44 MB Beats 23.94%---------------------------------------


class Solution:

    def reverse(self, head: ListNode) -> ListNode:
        if head:
            new_head = head
            if head.next:
                new_head = self.reverse(head.next)
                head.next.next = head
            head.next = None
            return new_head

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = self.reverse(head)
        h = rev
        prev = 0
        prev_node = None
        while rev:
            origin_val = rev.val * 2 + prev
            val = origin_val

            if val > 9:
                prev, val = divmod(val, 10)
            prev = 1 if origin_val > 9 else 0
            rev.val = val
            prev_node = rev
            rev = rev.next
        if prev:
            prev_node.next = ListNode(prev)

        return self.reverse(h)
