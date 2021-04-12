from typing import List
class Solution:
    def sell(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 0):
            return 0
        dp = [0] * n #Create an array with n zeroes
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) 
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]) #Recurrence relation
        #Print the list of selected houses
        nextSelected = False
        for i in range(n-1,0,-1):
            if (nextSelected == False) and (dp[i] > dp[i-1]):
                print(i, " is selected", "Sales=",nums[i])
                nextSelected = True
            else: nextSelected = False
        if nextSelected == False:
            print(0, " is selected", "Sales=",nums[0])
        return dp[n-1]
sol = Solution()
print("Total sale=",sol.sell([2,7,9,3,1]))