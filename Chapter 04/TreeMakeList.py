from typing import List
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
def makeTree(arr:List[int])-> TreeNode:
    n = len(arr)
    root = None
    return NodeInsert(arr,root,0,n)
def NodeInsert(arr:List[int],root:TreeNode,i:int,n:int)-> TreeNode: 
    if i<n:
        temp = TreeNode(arr[i])  
        root = temp  
        # insert left child  
        root.left = NodeInsert(arr, root.left, 2 * i + 1, n)  
        # insert right child  
        root.right = NodeInsert(arr, root.right, 2 * i + 2, n) 
    return root

root = makeTree([1,2,3,4,5,6,7])
printTree(root)