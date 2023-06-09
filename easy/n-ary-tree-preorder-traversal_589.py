class List(list):
    ...


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# My solution


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        counter = []
        if not root:
            return root
        value = root.val
        children = root.children
        if not children:
            return [value]
        counter.append(value)

        counter.extend(map(lambda x: self.preorder(x), children))
        output = []
        for i in counter:
            if isinstance(i, list):
                output.extend(i)
            else:
                output.append(i)
        return output


# Solution shivam_1110
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        ans = []

        def helper(curr=root):
            nonlocal ans
            if curr:
                ans.append(curr.val)
                for i in curr.children:
                    helper(i)

        helper()
        return ans
