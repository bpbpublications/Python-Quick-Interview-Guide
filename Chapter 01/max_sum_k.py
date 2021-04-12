import timeit
import random
from matplotlib import pyplot as plt
'''
class Solution():#Brute force
    def maxsumk(self, nums,k):
       maxsum = -1e6
       for i in range(len(nums)-k+1):
           curr_sum = 0
           for j in range(i,i+k):
               curr_sum += nums[j]
           maxsum = max(maxsum, curr_sum)
       return maxsum
'''
class Solution():#Sliding window
    def maxsumk(self, nums,k):
       maxsum = -1e6
       curr_sum = 0
       for j in range(k):
               curr_sum += nums[j]
       for i in range(1,len(nums)-k+1):
           curr_sum = curr_sum - nums[i-1] + nums[i+k-1]
           maxsum = max(maxsum, curr_sum)
       return maxsum

sol = Solution()
nums = [80,-50,90,100]
k=2
#print(sol.maxsumk(nums,2))
su='''
from __main__ import sol,nums,k;
'''
x=[]
y=[]   
for i in range(4,100):
    nums=[]
    k=i//2
    for j in range(i):
        nums.append(random.randint(3,10))
        #print(nums)
    t=timeit.timeit('sol.maxsumk(nums,k)',setup=su,number=100)
    x.append(i)
    y.append(t)
plt.plot(x,y)
plt.xlabel("N->")
plt.ylabel("time")
plt.title("Time complexity of efficient max sub array function")

