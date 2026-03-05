from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        current = 0

        def dsf(node, current):
            if not node:
                return 0
            
            current = 10*current + node.val

            if not node.left and not node.right:
                return current
            
            return dsf(node.left, current) + dsf(node.right, current)
        
        return dsf(root, 0)