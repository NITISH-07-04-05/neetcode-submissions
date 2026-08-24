# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(low,root,high):
            if root is None:
                return True

            if not (low<root.val<high):
                return False

            return validate(low,root.left,root.val) and validate(root.val,root.right,high)




        return validate(float('-inf'),root,float("inf"))
        