# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def good(root,max_so_far):
            if root is None:
                return 0

            count = 0

            if root.val >= max_so_far:
                count = 1
                max_so_far = root.val

            count +=good(root.left,max_so_far)
            count +=good(root.right,max_so_far)

            return count

        return good(root,root.val)
