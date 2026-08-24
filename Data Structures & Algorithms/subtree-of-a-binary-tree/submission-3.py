# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False

        def subtree(node , subnode):
            if node is None and subnode is None:
                return True

            if node is None and subnode is not None or node is not None and subnode is None:
                return False

            if node.val != subnode.val:
                return False


            return subtree(node.left,subnode.left ) and subtree(node.right,subnode.right)

        if subtree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
