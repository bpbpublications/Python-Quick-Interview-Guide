class MinStack:

    
    def __init__(self):
        self.stk = []          #Create empty stack
    def push(self, x: int) -> None:
        self.stk.append(x)
    def pop(self) -> None:
        self.stk.pop()
    def top(self) -> int:
        return self.stk[-1]
    def getMin(self) -> int:
        mini = float('inf')
        for n in self.stk:
            mini=min(mini,n)
        return mini
    
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stk)
print(obj.getMin())
obj.pop()
print(obj.stk)
print(obj.getMin())