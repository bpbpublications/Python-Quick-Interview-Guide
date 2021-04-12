# Definition for a binary tree node.
class TreeNode:
     def __init__(self, v):
         self.val = v
         self.left = None
         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    
    def isMirror(self,tree1,tree2):
        if(tree1 is None and tree2 is None):
            return True
        if(tree1 is None or tree2 is None):
            return False
        return (tree1.val==tree2.val)\
            and self.isMirror(tree1.right,tree2.left) \
            and self.isMirror(tree1.left,tree2.right)
root = TreeNode(1) 
root.left = TreeNode(4) 
root.right = TreeNode(4) 
root.left.left = TreeNode(5) 
root.left.right = TreeNode(6) 
root.right.left = TreeNode(6) 
root.right.right = TreeNode(5) 
sol = Solution()
print(sol.isSymmetric(root))