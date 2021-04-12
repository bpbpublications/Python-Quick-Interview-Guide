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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        sorted = []
        def printInorder(root): 
            if root: 
                #rv=root.val
                printInorder(root.left) #Recursively call left child
                #print(root.val)
                sorted.append(root.val) #Append node value
                printInorder(root.right) #Recursively call right child
        printInorder(root)
        return sorted[k-1]
#Driver code 

root = TreeNode(5) 
root.left = TreeNode(3) 
root.right = TreeNode(6) 
root.left.left = TreeNode(2) 
root.left.right = TreeNode(4) 
root.right.left = TreeNode(None) 
root.right.right = TreeNode(7) 
bst = BinTree()
bst.printTree(root)
sol = Solution()
print("kth smallest=",sol.kthSmallest(root,2))
