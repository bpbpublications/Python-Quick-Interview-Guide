class MinStack:
    def __init__(self):
        self.stk = []          #Create empty stack
        self.mini = float('inf')
    def push(self, x: int) -> None:
        if x<=self.mini:            #If new value is less than mini
           self.stk.append(self.mini) #Then save old value of mini on stack
           self.mini = x              #Update mini
        self.stk.append(x)       #Append new element
    def pop(self) -> None:
        stktop=self.stk[-1]             
        self.stk.pop()
        if self.mini == stktop:
            self.mini = self.stk[-1]
            self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mini
    
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stk)
print(obj.getMin())
obj.pop()
print(obj.top)
print(obj.stk)
print(obj.getMin())