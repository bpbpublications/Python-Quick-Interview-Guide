
class Solution:#Linear search
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:return True
        for i in range(1,num//2 + 1):
            if num == i*i: return True
        return False
'''
class Solution:#Arithmetic progression
    def isPerfectSquare(self, num: int) -> bool:
        sum = 0;i=1
        while sum < num: 
            sum += i 
            if sum == num:return True
            i += 2
        return False
'''
#Driver code        
sol=Solution()
for i in range(1,10):
    print(i,sol.isPerfectSquare(i))