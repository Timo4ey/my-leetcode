# Companies
# Given the head of a singly linked list, return true if it is a
# palindrome
#  or false otherwise.

# Example 1:

# ￼
# Input: head = [1,2,2,1]
# Output: true
# Example 2:

# ￼
# Input: head = [1,2]
# Output: false

# ---------------------------------------Runtime 763 ms Beats 68.33% Memory 49 MB Beats 50.61%---------------------------------------
# Time complexity O(n)


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        store: list = []
        node: ListNode = head
        while node:
            store.append(node.val)
            node = node.next
        return store == store[::-1]
