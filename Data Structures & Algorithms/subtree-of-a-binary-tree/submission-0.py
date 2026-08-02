# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(root,subroot):
            if root is None and subroot is not None:
                return False

            if root is not None and subroot is None:
                return False

            if root is None and subroot is None:
                return True
            
            if root.val != subroot.val:
                return False


            return sametree(root.left,subroot.left) and sametree(root.right,subroot.right)
        if root is None:
            return False

        if subRoot is None:
            return True

        if sametree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        

            
        