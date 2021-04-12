'''
class Solution:#Recursive
    def tribonacci(self, n: int) -> int:
        if n==2:return 1
        if n<2 :return n
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

class Solution:#iterative
    def tribonacci(self, n: int) -> int:
        if n==2:return 1
        if n<2 :return n
        tn_3 = 0
        tn_2 = 1
        tn_1 = 1
        for i in range(3,n+1):
            trib = tn_1 + tn_2 + tn_3
            tn_3 = tn_2
            tn_2 = tn_1
            tn_1 = trib
        return trib
'''
from functools import lru_cache 
class Solution:
    @lru_cache(None) #Store data in cache for next calls
    def tribonacci(self, n: int) -> int:
        if n==0: return 0
        if n<3:  return 1
        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
#Driver code
sol=Solution()
print(sol.tribonacci(30))