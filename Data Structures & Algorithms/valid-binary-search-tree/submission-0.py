# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        val = True
        if root.left is None:
            return

        if root.right is None:
            return 
        if root.left.val > root.val or root.right.val < root.val:
            return False

        self.isValidBST(root.right)
        self.isValidBST(root.right)

        return val