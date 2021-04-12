from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        #Nested helper function
        def dfs(partial, index):
            print("On entry partial=",partial,"index=",index)
            if len(partial) == k:
                print("Appended ",partial,index)
                res.append(partial)
                return
            #Call dfs for all values of i
            #Backtrace to same after return from dfs 
            for i in range(index, n+1):
                print("Before ",partial,"i=",i,"Ind=",index)
                dfs(partial + [i], i+1)
                print("After ",partial,"i=",i,"Ind=",index)
            print("Returning")
        #Resume main function   
        dfs([], 1)
        
        return res
#Driver code
sol=Solution()
print(sol.combine(4,3))
