# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class List(list):
    ...


class Optional(List):
    ...


# My Solution

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        gather = []
        gather.append([root.val])
        q = deque()
        q.extend([root.left, root.right])
        while q:
            store = []
            temp = [[]]
            counter = 0
            for node in q:
                if isinstance(node, TreeNode):
                    temp[0].append(node.val)
                    store.extend([node.left, node.right])
                counter += 1

            if temp[0]:
                gather.extend(temp)
            temp.clear()
            if store:
                q.extend(store)
            for x in range(counter):
                q.popleft()

        return gather
