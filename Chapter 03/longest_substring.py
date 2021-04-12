import timeit
import random
from matplotlib import pyplot as plt
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:return len(s)
        longcount = 0
        for l in range(len(s)):
            ss = set()
            for r in range(l,len(s)):
                if s[r] not in ss:
                    ss.add(s[r])
                    longcount = max(longcount,len(ss))
                else:
                    longcount = max(longcount,len(ss))
                    break
        return longcount   
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        for right in range(len(s)):
            el = s[right]
            if(el in m):
                left = max(left,m[el]+1)
            m[el] = right
            ans = max(ans,right-left+1)
        return ans

sol = Solution()
s = "abcadefcg"  
print(sol.lengthOfLongestSubstring(s))
su='''
from __main__ import sol,nums,k;

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
'''
