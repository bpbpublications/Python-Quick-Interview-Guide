from typing import List
class TreeNode:
     def __init__(self, v):
         self.val = v
         self.left = None
         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:return root
        q = []
        List = []
        q.append(root)
        while len(q):
            LvlList = []
            for i in range(len(q)):
                node = q.pop(0)
                LvlList.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            List.append(LvlList)
        return List
def makeTree(arr:List[int])-> TreeNode:
    return NodeInsert(arr,None,0)
def NodeInsert(arr:List[int],root:TreeNode,i:int)-> TreeNode: 
    n=len(arr)
    if i<n:
        root = TreeNode(arr[i])
        # insert left child  
        root.left = NodeInsert(arr, root.left, 2 * i + 1)  
        # insert right child  
        root.right = NodeInsert(arr, root.right, 2 * i + 2) 
    return root

root = makeTree([1,2,3,4,5,6,7,None,None,8,9,None,None,None,None])
sol=Solution()
L = sol.levelOrder(root)
print(L)