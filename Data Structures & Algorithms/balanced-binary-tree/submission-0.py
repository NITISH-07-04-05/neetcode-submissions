# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(root):
            if root is None:
                return 0

            if root == -1:
                return -1


            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) >1:
                return -1

            return 1 + max(left,right)
        
        if dfs(root) == -1:
            return False

        return True

