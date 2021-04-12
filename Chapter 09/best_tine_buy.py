from typing import List  #Not needed when submitting to Leet code
'''
class Solution:     #Brute force method
    def maxProfit(self, prices: List[int]) -> int:
        mprof = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                mprof = max(mprof, prices[j]-prices[i])
        return mprof
 '''
class Solution:     #Better method
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = 1e6               #Initially loest valley is set very high
        profit = 0
        for i in range(len(prices)):
            if(prices[i] < buyPrice):
                buyPrice = prices[i]
            else:
                profit = max(profit, prices[i]-buyPrice)
        return profit               
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4] ))