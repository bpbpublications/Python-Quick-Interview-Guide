from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.dest = {}                  #Create empty graph of source:destinations
        tickets.sort(key=lambda x:x[1]) #Sort tickets based on destination
        for u,v in tickets:
            if u in self.dest: self.dest[u].append(v)#If u exists, add v to list
            else: self.dest[u] = [v]    #u does not exist, so create a new list
        self.path = []                #Create empty list for storing path
        self.dfs("JFK")                 #Start depth first search 
        return self.path[::-1]        #Reverse the order in path
    
    def dfs(self,s):
        #scan destination list of source s as long as it is not empty
        
        while s in self.dest and len(self.dest[s]) > 0:
            ds=self.dest[s]
            dl=ds[0]
            v = self.dest[s][0]     #v = top of destination list
            self.dest[s].pop(0)     #Remove it from list (pop from left)
            self.dfs(v)             #Recursively call v
        self.path.append(s)         #Add s to path
            
#Driver code
sol= Solution()
#tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#tickets =[["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
tickets =[["JFK","SIN"],["JFK","BOM"],["SIN","BOM"],["BOM","JFK"],["BOM","SIN"]]
print(tickets)
print(sol.findItinerary(tickets))
 