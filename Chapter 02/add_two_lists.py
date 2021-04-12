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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        pointer = ans               #Pointer in answer string
        carry = 0;                  #To begin with, carry is 0
        while(l1!=None or l2!=None):#Keep looping l1 and l2 are not finished
            sum = carry             #Initialize sum with last iteration's carry
            if(l1!=None):
                sum+=l1.val         #If l1 is not finished, add l1.val to sum
                l1 = l1.next        #Advance l1 to next element
            if(l2!=None):
                sum+=l2.val         #if l2 is not finished, add l2.val to sum
                l2 = l2.next        #Advance l2 to next element
            carry = sum//10         #integer division
            pointer.next  = ListNode(sum%10)#create new node with sum modulo 10
            pointer = pointer.next  #Advance the answer pointer
        if carry:                   #If last addition creates carry, 
            pointer.next = ListNode(carry)#Create one more node and add it
        return ans.next
    #driver code
n11 = ListNode(1);n12=ListNode(3);n13=ListNode(5)
n11.next = n12;n12.next = n13
n21 = ListNode(2);n22=ListNode(4);n23=ListNode(6)
n21.next = n22;n22.next = n23
sol=Solution()
add = sol.addTwoNumbers(n11,n21)
display(add)
