from typing import List
from collections import deque
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
def printTree(root:TreeNode)->None:
    LevelList = [root]
    printLevel(LevelList)
    
def printLevel(LevelList:List[TreeNode])-> List[TreeNode]:
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
        printLevel(outList)
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque()
        q.append((root,0))
        par_depth={}
        while q:
            node,depth = q.popleft()
            if node.left:
                par_depth[node.left.val]=(node.val,depth+1)
                q.append((node.left,depth+1))
            if node.right:
                par_depth[node.right.val]=(node.val,depth+1)
                q.append((node.right,depth+1))
            if (x in par_depth) and (y in par_depth):break
        if x not in par_depth or y not in par_depth: return False
        x_parent,x_depth = par_depth[x]
        y_parent,y_depth = par_depth[y]
        return x_depth == y_depth and x_parent != y_parent    

root =TreeNode(1) 
root.left =TreeNode(2) 
root.right =TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right =TreeNode(5) 
root.right.left =TreeNode(6) 
root.right.right =TreeNode(7)
printTree(root)

sol = Solution()
print(sol.isCousins(root,5,6))
