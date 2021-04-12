from typing import List
import numpy as np  
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp = np.zeros((n+1,2))
        
        for i in range(1,len(cost)+1):
            dp[i][0] = min(dp[i-1][0] , dp[i-1][1])+ cost[i-1]#Taking curr step
            dp[i][1] = dp[i-1][0] # not taking current step
            
        return int(min(dp[n][0], dp[n][1]))    
           
sol = Solution()
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    
