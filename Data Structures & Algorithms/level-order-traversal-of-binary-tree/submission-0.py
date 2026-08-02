# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        q = deque([root])
        output.append([root])
        while q:
            level = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)

                output.append(level)

        return output