# https://leetcode.com/problems/merge-two-sorted-lists/


# My solution
### Notes i tried to solve this task user a recursion approach
###


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
