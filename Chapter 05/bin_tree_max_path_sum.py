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
    ans = -float("inf")
    def solution(self,node):
        v=node.val if node is not None else 0
        if(node is None):
            return 0
        left = self.solution(node.left)
        right = self.solution(node.right)
        nv = node.val if node.val is not None else 0
        mxSide = max(nv,max(left,right)+nv)
        mxTop = max(mxSide,left+right+nv)
        self.ans = max(self.ans,mxTop)
        return mxSide

    def maxPathSum(self, root: TreeNode) -> int:
        self.solution(root)
        return self.ans
#Driver code 
'''
root = TreeNode(5) 
root.left = TreeNode(3) 
root.right = TreeNode(6) 
root.left.left = TreeNode(2) 
root.left.right = TreeNode(4) 
root.right.left = TreeNode(None) 
root.right.right = TreeNode(7) 
'''
root = TreeNode(8) 
root.left = TreeNode(3) 
root.right   = TreeNode(10); 
root.left.left  = TreeNode(20); 
root.left.right = TreeNode(1); 
root.right.right = TreeNode(-25); 
root.right.right.left   = TreeNode(4); 
root.right.right.right  = TreeNode(5);

bst = BinTree()
bst.printTree(root)
sol = Solution()
print("Max path sum=",sol.maxPathSum(root))
