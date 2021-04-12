from typing import List
def display(root): 
    while (root != None) : 
        print(root.val, end = " ") 
        root = root.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #l1 and l2 are initially roots of the two input lists
        #As we will append the current element to output, we will advance them
        cur = ListNode(0)   #Create an empty node for output list
        ans = cur           #ans remembers starting position
        while(l1 and l2):   #Execute this till both lists have elements
            if(l1.val>l2.val):
                cur.next = l2 #If l2 is smaller, insert it in current
                l2 = l2.next  #Advance the pointer for l2
            else:
                cur.next = l1 #If l1 is smaller, insert it in current
                l1 = l1.next  #Advance the pointer for l2
            cur = cur.next    #Advance the pointer for current
        while(l1):            #Execute this if l1 is not finished
                cur.next = l1 #Append l1 element to cur
                l1 = l1.next  #Advance the pointer for l1
                cur = cur.next
		
        while(l2):
                cur.next = l2
                l2 = l2.next  #Advance the pointer for l2
                cur = cur.next#Advance the pointer for current
        return ans.next       #next field of ans is head of cur list
#driver code
n11 = ListNode(1);n12=ListNode(3);n13=ListNode(5)
n11.next = n12;n12.next = n13
n21 = ListNode(2);n22=ListNode(4);n23=ListNode(6)
n21.next = n22;n22.next = n23

sol=Solution()
merg = sol.mergeTwoLists(n11,n21)
display(merg)
