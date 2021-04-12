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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(not head):               #If head is invalid, return immediately
            return head

        odd = head                 #odd = iterator of odd series
        even = odd.next            #even = iterator of even series
        evenList = even            #Start of even series

        while(even and even.next):
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenList       #Append start of even series to end of odd
        return head
n1=ListNode(11);n2=ListNode(12);n3=ListNode(13);n4=ListNode(14);n5=ListNode(15)
n1.next = n2;n2.next = n3;n3.next = n4;n4.next=n5;n5.next = None
display(n1)
sol=Solution()
r=sol.oddEvenList(n1)
display(r)