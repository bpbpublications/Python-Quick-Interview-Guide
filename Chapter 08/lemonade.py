from typing import List
class Solution:
    def lemonadeChange(self, notes: List[int]) -> bool:
        five = ten = 0      #Initial number of 5 and 10 notes
        for note in notes:  #Scan the array
            if note == 5:   #If you get Rs 5 note, keep it
                five += 1   #Increment stock of 5's
            elif note == 10:#Suppose you get Rs 10 note
                if not five: return False#If you don't have stock of Rs 5, false
                five -= 1   #Return 5 and decrement its stock
                ten += 1    #Increment stock of 10's
            else:           #Suppose you get Rs 20 note
                if ten and five:#If you have both 10 and 5 in stock
                    ten -= 1    #Return 10
                    five -= 1   #Return 5
                elif five >= 3: #If you have 3 or more 5's
                    five -= 3   #Return 3 5's
                else:
                    return False
        return True
#Driver code
sol = Solution()
print(sol.lemonadeChange([5,5,5,10,20]))