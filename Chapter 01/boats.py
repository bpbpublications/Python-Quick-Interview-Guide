#from typing import List  #Not needed when submitting to Leet code
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort() # Arrange weights in ascending order
        print(people)
        low=0 ;#Set up a pointer at low end
        high=len(people) - 1 # Set up pointer at high end
        n_boats = 0 #Initialize boats counter to 0
        # We pinch the array between advancing low & reducing high
        #When low reaches high, we finish
        while low <= high: 
            n_boats += 1 # Take a new boat
            #Heavy person takes the boat, so always decrement high 
            #If boat can take accomodate a light person, increment low
            if people[low] + people[high] <= limit:
                low += 1
            high -= 1
        return n_boats
people = [3,2,2,1]
limit = 3
sol = Solution()
print(sol.numRescueBoats(people, limit))
      
  