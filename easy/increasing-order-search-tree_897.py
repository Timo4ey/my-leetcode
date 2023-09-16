# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.


# Example 1:

# ￼
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Example 2:

# ￼
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]

# ---------------------------------------Runtime 35 ms Beats 82.56% Memory 16.4 MB Beats 68.40%---------------------------------------


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes: list[TreeNode] = []

        def dfs(node: TreeNode) -> None:
            if node:
                nodes.append(node)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        nodes.sort(key=lambda x: x.val)

        for indx in range(len(nodes) - 1):
            nodes[indx].left = None
            nodes[indx].right = nodes[indx + 1]
        nodes[-1].left = None
        nodes[-1].right = None

        return nodes[0]
