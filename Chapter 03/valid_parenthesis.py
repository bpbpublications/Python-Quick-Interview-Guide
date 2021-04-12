class Solution:
    def isValid(self, s: str) -> bool:
        brac_match = {')':'(', ']':'[', '}':'{'}
        openers = ['(', '[', '{']
        stk = []#Define array to act as a stack
        for char in s:
            if char in openers:
                stk.append(char)#If char is opening bracket, push it on stack
            elif [] == stk:
                return False#if stack is empty when closing comes, it is False condition
            elif stk[-1] == brac_match[char]:
                stk.pop()
            else :
                return False
        return [] == stk#If you end up in empty stack, return True
sol = Solution()
print(sol.isValid("([])"))
