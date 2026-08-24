# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        output = []
        while queue:
            length = len(queue)
            temp = []

            for _ in range(length):
                value = queue.popleft()
                temp.append(value.val)

                if value.left:
                    queue.append(value.left)

                if value.right:
                    queue.append(value.right)

            output.append(temp)

        return output