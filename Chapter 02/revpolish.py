from typing import List
#define lambda functions
ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: int(a / b))
}
class Solution:
 def evalRPN(self, expression: List[str]) -> int:
  stack = []
  
  for token in expression: #Examine each token
    if token in ops:            #If token is an operator
      arg2 = stack.pop()        #Then pop two elements from the stack
      arg1 = stack.pop()
      result = ops[token](arg1, arg2)#Perform the operation
      stack.append(result)           #Push the result on stack
    else:
      stack.append(int(token))       #If token is not operator, push it on stack

  return stack.pop()     # In the end, stack top contains the answer
sol = Solution() 

print(sol.evalRPN(["2", "5", "+", "3", "*"]))
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
