# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        u = set()
        stack = [root]
        while stack:
            if node := stack.pop():
                u.add(node.val)
                stack += node.right, node.left

        return -1 if len(u) < 2 else sorted(u)[1]
