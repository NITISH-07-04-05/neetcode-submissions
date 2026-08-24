# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0 
        output = []
        def inorder(root):
            if root is None or len(output) == k:
                return 

            inorder(root.left)
            output.append(root.val)
            inorder(root.right)

        inorder(root)
        return output[k-1]