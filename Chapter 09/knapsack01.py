class Solution:
    def knapSack(self,W, wt, val): 
        n = len(val) 
        K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
        # Build table K[][] in bottom up manner 
        for i in range(1,n + 1): 
            for w in range(W + 1): 
                
                if i == 0 or w == 0: 
                    K[i][w] = 0
                elif wt[i-1] <= w: 
                    K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
                else: 
                    K[i][w] = K[i-1][w] 
                

#Find list of selected items 
        i=n
        j=W     #Bottom right corner
        V = K[i][j]
        while V:
            while i:
                if K[i][j] > K[i-1][j]: 
                    print(i-1, ' Selected')
                    break
                else:i -= 1
            i-= 1
            j -= wt[i]
            V -= val[i]
        return K[n][W] 
#Driver program to test above function 
sol=Solution()
'''
val = [60, 100, 120] 
wt = [10, 20, 30]   
W = 50 #Ans 220
print(sol.knapSack(W, wt, val)) 
val = [1,2,5,6] 
wt = [2,3,4,5]   
W = 8 #Ans 8
print(sol.knapSack(W, wt, val)) 
'''
val = [60,50,70,30] 
wt = [5,3,4,2]   
W = 5 #Ans 80
print(sol.knapSack(W, wt, val)) 
