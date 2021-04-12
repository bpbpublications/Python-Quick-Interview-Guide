
class Solution:
    def mySqrt(self, x: int) -> int:
        # Base cases 
        if (x == 0 or x == 1): 
            return x 
        # Staring from 1, try all numbers until 
        # i*i remains less than to x. 
        i = 1
        while (i*i < x):i += 1
        return i if i*i == x else i-1
'''
class Solution:
  def mySqrt(self,x) : 
  
    # Base cases 
    if (x == 0 or x == 1) : 
        return x 
   
    # Do Binary Search for integer square root
    start = 1
    end = x    
    while (start <= end) : 
        mid = (start + end) // 2
          
        # If x is a perfect square 
        if (mid*mid == x) : 
            return mid 
              
        # when mid^2 is smaller than x, check if (mid+1)^2 >x
        if (mid * mid < x) : 
            if (mid+1)*(mid+1) > x:return mid
            start = mid + 1
              
        else : 
              
            # If mid*mid is greater than x 
            end = mid-1
'''

sol=Solution()
for i in range(1,10):
    print(i,sol.mySqrt(i))
