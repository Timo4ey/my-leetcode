# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# ￼
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:

# ￼
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# ---------------------------------------Runtime 33 ms Beats 86.53% Memory 13.8 MB Beats 100%---------------------------------------

# https://leetcode.com/problems/middle-of-the-linked-list/description/


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# My solution


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fst, count = head, -1

        while head.next:
            count += 1
            head = head.next
        target = count // 2 + 1
        new_count = 0
        while new_count != target:
            new_count += 1
            fst = fst.next

        return fst


# Approach 2: Fast and Slow Pointer
"""
Intuition and Algorithm

When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. 
When fast reaches the end of the list, slow must be in the middle

Complexity Analysis

Time Complexity: O(N), where N is the number of nodes in the given list.

Space Complexity: O(1), the space used by slow and fast.
"""


class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# My comments to me in the future :)
# fast just to times faster
# omg thats so genius
