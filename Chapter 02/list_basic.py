class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def display(root): 
    while (root != None) : 
        print(root.val, end = " ") 
        root = root.next
    print('\n')
        
n1=ListNode(1)
n2=ListNode(3)
n3=ListNode(5)
n1.next=n2
n2.next=n3
display(n1)

n4=ListNode(10)
n4.next=n1
display(n4)

n5=ListNode(20)
n=n1
while n.next:
    n=n.next
n.next=n5
display(n1)

def MakeList(a):
    root = ListNode(a[0])
    cur = root
    for i in range(1,len(a)):
        temp = ListNode(a[i])
        cur.next = temp
        cur = cur.next
    return root    

MyList = MakeList([1,2,3,4,5])
display(MyList)
    
