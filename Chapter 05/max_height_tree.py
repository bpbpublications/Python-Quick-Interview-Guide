# Definition for a binary tree node.
class TreeNode:
     def __init__(self, v):
         self.val = v
         self.left = None
         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root is None):
            return 0
        if(root.left is None and  root.right is None):
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right)+1
root = TreeNode(2) 
root.left = TreeNode(9) 
root.right = TreeNode(20) 
root.left.left = TreeNode(None) 
root.left.right = TreeNode(None) 
root.right.left = TreeNode(15) 
root.right.right = TreeNode(6) 
sol = Solution()
print(sol.maxDepth(root))