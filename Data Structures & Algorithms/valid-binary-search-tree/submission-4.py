# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None or root.right is None or root.left is None:
            return True

        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)

        if root.left.val > root.val or root.right.val < root.val:
            return False

        return left and right 
        