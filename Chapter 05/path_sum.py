# Definition for a binary tree node.
class TreeNode:
     def __init__(self, v):
         self.val = v
         self.left = None
         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.hasSum(root,sum, 0)
    def hasSum(self,root,sum,cur):
        if(root is None):
            return False
        if root.val == None:rv=0
        else:rv=root.val
        cur+=rv
        if(cur==sum and root.left is None and root.right is None):
            return True
        return (self.hasSum(root.right,sum,cur) or self.hasSum(root.left,sum,cur))
#Driver code    
root = TreeNode(5) 
root.left = TreeNode(4) 
root.right = TreeNode(8) 
root.left.left = TreeNode(11) 
root.right.left = TreeNode(13) 
root.right.right = TreeNode(4) 
root.left.left.left = TreeNode(7) 
root.left.left.right = TreeNode(2) 
root.right.left.right = TreeNode(1) 
sol = Solution()
print(sol.hasPathSum(root,27))
print(sol.hasPathSum(root,22))
print(sol.hasPathSum(root,17))