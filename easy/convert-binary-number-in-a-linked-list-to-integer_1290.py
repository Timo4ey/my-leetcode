# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1
# The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.


# Example 1:

# ￼
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
# ---------------------------------------Runtime 44 ms Beats 70.64% Memory 16.3 MB Beats 56.34%---------------------------------------


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity O(n)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans: list = [str(head.val)]
        node: ListNode = head.next
        while node:
            ans.append(str(node.val))
            node = node.next
        return int("".join(ans), base=2)
