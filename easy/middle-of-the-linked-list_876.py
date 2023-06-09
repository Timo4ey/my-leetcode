# https://leetcode.com/problems/middle-of-the-linked-list/description/


class Optional(list):
    ...


# Definition for singly-linked list.
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
