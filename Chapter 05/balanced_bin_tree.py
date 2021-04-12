from typing import List
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
class BinTree:
    def printTree(self,root:TreeNode)->None:
        LevelList = [root]
        self.printLevel(LevelList)
    def printLevel(self,LevelList:List[TreeNode])-> List[TreeNode]:
        LevelStr = ""
        outList = []
        ListEmpty = True
        for node in LevelList:
            if node is None:
                LevelStr += "None "
                outList.append(None)
                outList.append(None)
            else:
                LevelStr += (str(node.val) + " ")
                outList.append(node.left)
                outList.append(node.right)
                ListEmpty = False
        if not ListEmpty:
            print(LevelStr)
            self.printLevel(outList)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #Nested function to find depth. (-1) denotes unbalanced
        def depth(root: TreeNode) -> int:
            rv = root.val if root else 0
            if not root: return 0       #Depth is 0 if node is None
            ldepth = depth(root.left)   #Find depth of left subtree
            rdepth = depth(root.right)  #Find depth of right subtree
            if ldepth == -1 or rdepth == -1 or abs(ldepth - rdepth) > 1:
                return -1
            return max(ldepth, rdepth) + 1 #Depth of root = sub trees+1
        dr = depth(root)
        return dr != -1
#Driver code    
root = TreeNode(8) 
root.left = TreeNode(3) 
root.right   = TreeNode(10) 
root.left.left  = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left   = TreeNode(4)
root.right.right.right  = TreeNode(5)

bst = BinTree()
bst.printTree(root)
sol = Solution()
print("Tree is balanced?",sol.isBalanced(root))