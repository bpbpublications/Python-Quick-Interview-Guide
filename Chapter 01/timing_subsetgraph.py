import timeit
import random
from matplotlib import pyplot as plt
from typing import List  
a=[]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            new_output = []
            for curr in output:
                new_output += [curr + [num] ]
            output += new_output
        return output
sol = Solution()

su='''
from __main__ import sol,a
'''  
x=[]
y=[]  
for i in range(3,15):
    a=[] 
    for j in range(i):
        a.append(random.randint(1,100))
    t=timeit.timeit('sol.subsets(a)',setup=su,number=100)
    x.append(i)
    y.append(t)
plt.plot(x,y)
plt.xlabel("N->")
plt.ylabel("time")
plt.title("Time complexity of subset function")
    
 