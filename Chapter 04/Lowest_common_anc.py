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

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Create Stack of nodes to be traversed
        stack = [root]      #Initially it only has root
        # Create a Dictionary to store traversed parent pointers
        parent = {root: None}
        p_not_found = True
        q_not_found = True
        # Keep looping until both p and q are added parent dictionary
        while p_not_found or q_not_found:
            node = stack.pop()
            if node == p: p_not_found = False
            if node == q: q_not_found = False
            # If child exists, add it to stack and mark node as its parent
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        #Parent dictionary is ready
        # Create Ancestors set for node p.
        ancestors = set()
        # Find all ancestors of p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]
        # Ascend hiearchy of q. The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
root = n1=TreeNode(1) 
root.left = n2=TreeNode(2) 
root.right = n3=TreeNode(3) 
root.left.left = n4= TreeNode(4) 
root.left.right = n5=TreeNode(5) 
root.right.left = n6=TreeNode(6) 
root.right.right = n7=TreeNode(7)
n5.left=n8=TreeNode(8)
n5.right=n9=TreeNode(9)         
printTree(root)

sol = Solution()
print("ans ",sol.lowestCommonAncestor(root,n8,n6).val)
print("ans ",sol.lowestCommonAncestor(root,n4,n5).val)
print("ans ",sol.lowestCommonAncestor(root,n6,n7).val)
