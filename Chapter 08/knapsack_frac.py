class ItemValue: 
      
    #Class to store items data
    def __init__(self, wt, val, index): 
        self.wt = wt        #Weight of item
        self.val = val      #Value of item
        self.index = index  #Index of item in list
        self.cost = val / wt #Figure of merit
  
    def __lt__(self, other): 
        return self.cost < other.cost #Needed for sort function
  
# Greedy Approach 
class Solution: 
    def getMaxKnapsack(self,wt, val, capacity): 
        #From the given weoght and value arrays, 
        #prepare an array of ItemVaue objects
        iVal = [] 
        for i in range(len(wt)): 
            iVal.append(ItemValue(wt[i], val[i], i)) 
        # Sort ItemValue array according to figure of merit, max first
        iVal.sort(reverse = True) 
        totalValue = 0                  #Initialize total value to 0
        for i in iVal:
            iwt=i.wt
            ival=i.val
            ind=i.index
            if capacity >= iwt: 
                capacity -= iwt 
                totalValue += ival 
                print('Index =',i.index,'value=',ival,'Full')
            else: 
                fraction = capacity / iwt 
                totalValue += ival * fraction 
                print('Index =',i.index,'value =', 
                      ival*fraction,'Fraction',fraction)
                break
        return totalValue 
  
# Driver Code 
wt = [10, 40, 20, 30] 
val = [60, 40, 100, 120] 
capacity = 50
sol=Solution() 
maxValue = sol.getMaxKnapsack(wt, val, capacity) 
print("Maximum value in Knapsack =", maxValue) 
  