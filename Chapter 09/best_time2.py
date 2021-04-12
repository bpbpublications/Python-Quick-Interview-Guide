from typing import List  
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1] :
                ans+=(prices[i] - prices[i-1])
        return ans
sol = Solution()

#print(sol.maxProfit([7,1,5,3,6,4]))
#print(sol.maxProfit([7, 6, 4, 3, 1]))
#print(sol.maxProfit([1, 2, 3 ,4, 5]))
print(sol.maxProfit([3, 7, 2, 3, 6, 7, 6, 7]))