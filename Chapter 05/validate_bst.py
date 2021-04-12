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
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            
            if  node is None: 
                print("Node is None")               #Diagnostic
                return True
            nl=node.left.val if node.left else 0    #Diagnostic
            nr=node.right.val if node.right else 0  #Diagnostic
            val = node.val                          #Diagnostic
            print(val,'\t',nl,'\t',nr,'\t',lower,'\t',upper)            #Diagnostic
            if not val: val = 0
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        print('val','\t','left','\t','right','\t','lower','\t','upper')   
        return helper(root)
#Driver code

root = TreeNode(2) 
root.left = TreeNode(1) 
root.right   = TreeNode(4) 
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
'''
root = TreeNode(5) 
root.left = TreeNode(1) 
root.right   = TreeNode(4) 
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

root = TreeNode(2) 
root.left = TreeNode(1) 
root.right   = TreeNode(3) 
'''
bst = BinTree()
bst.printTree(root)
sol = Solution()
print("Tree is valid?",sol.isValidBST(root))