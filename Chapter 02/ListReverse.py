#from typing import List
def display(root): 
    while (root != None) : 
        print(root.val, end = " ") 
        root = root.next
    print('\n')
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        Left = None             #Initialize left pointer to 0
        while(head is not None):#Scan the list with head (Current)
            Right = head.next   #Save  pointer of element to right of current
            head.next = Left    #Current element's next pointer = Left
            Left = head         #Current becomes Left in next iteration
            head = Right        #Advance current pointer to saved Right
        return Left
n1 = ListNode(1);n2=ListNode(2);n3=ListNode(3);n4=ListNode(4)
n1.next = n2;n2.next = n3;n3.next = n4;n4.next = None
display(n1)
sol=Solution()
r=sol.reverseList(n1)
display(r)