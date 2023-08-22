# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.


# Example 1:

# ￼
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:

# ￼
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

# ---------------------------------------Runtime 47 ms Beats 80.88% Memory 19 MB Beats 55.18%---------------------------------------


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution
# Time complexity O(n)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        slow, fast = head, head.next
        temp = None
        while slow and fast and fast.next:
            store.append(fast)
            temp = fast.next
            fast = fast.next.next
            slow.next = temp
            slow = slow.next
        if fast:
            store.append(fast)
        store.reverse()

        while store:
            slow.next = store.pop()
            if not store:
                slow.next.next = None
            slow = slow.next
        return head


# Solution @stanislav-iablokov
# Time complexity O(n)


class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        odd, evn, dum = head, head.next, head.next

        while evn and evn.next:
            odd.next, evn.next = odd, evn = odd.next.next, evn.next.next

        odd.next = dum

        return head
