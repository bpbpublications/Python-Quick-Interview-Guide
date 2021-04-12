# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Base case:if tree is empty  it is considered symmetric
        if (root == None) :return True
        # Base case:Single tree node with no children is considered symmetric 
        if(not root.left and not root.right):return True
      
        q = []     #Create empty queue of nodes 
        q.append(root);q.append(root) #Add root to queue two times 

        while(len(q)):  
            # Pop first two nodes from queue 
            # check their symmetry.  
            leftNode = q[0] ; q.pop(0)  
            rightNode = q[0] ;q.pop(0) 
            l=leftNode.val;r=rightNode.val
            # if both left and right nodes exisr but different values
            # then return False  
            if(leftNode.val != rightNode.val):return False
            #Left child of left  node and right child of right node
            # are symmetrical positions. Append them to queue 
            #Provided both exist
            if(leftNode.left and rightNode.right) : 
                q.append(leftNode.left)  
                q.append(rightNode.right)  
                # If only one of the two children is present  
                # then tree is not symmetric.  
            elif (leftNode.left or rightNode.right) :return False
                #Right child of left  node and left child of right node
                # are symmetrical positions. Append them to queue 
                #Provided both exist
            if(leftNode.right and rightNode.left):  
                q.append(leftNode.right)  
                q.append(rightNode.left)  
            # If only one of the two children is present  
            # then tree is not symmetric. 
            elif(leftNode.right or rightNode.left):return False
        return True
root = TreeNode(1) 
root.left = TreeNode(5) 
root.right = TreeNode(5) 
root.left.left = TreeNode(3) 
root.left.right = TreeNode(4) 
root.right.left = TreeNode(4) 
root.right.right = TreeNode(3) 
sol = Solution()
print(sol.isSymmetric(root))