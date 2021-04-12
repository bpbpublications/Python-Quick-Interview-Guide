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
     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        first = ans
        second = ans
        ans.next = head

        for i in range(n+1):
            first = first.next
            
        while(first is not None):
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return ans.next
n1 = ListNode(1);n2=ListNode(2);n3=ListNode(3);n4=ListNode(4);n5=ListNode(5)
n1.next = n2;n2.next = n3;n3.next = n4;n4.next=n5;n5.next = None
display(n1)
sol=Solution()
r=sol.removeNthFromEnd(n1,2)
display(r)