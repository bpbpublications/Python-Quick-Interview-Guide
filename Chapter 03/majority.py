'''
import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

class Solution:
    def majorityElement(self, nums):
        counts = {} 
        for items in nums: 
            counts[items] = nums.count(items) 
        return max(counts.keys(), key=counts.get)

class Solution:
    def majorityElement(self, nums): 
        counts = {} 
        for item in nums: 
            if (item in counts): 
                counts[item] += 1
            else: 
                counts[item] = 1
        return max(counts.keys(), key=counts.get)
'''
class Solution:
    def majorityElement(self, nums): 
        counts = {} 
        for item in nums: 
            counts[item] = counts.get(item, 0) + 1
        return max(counts.keys(), key=counts.get)
sol = Solution()
print(sol.majorityElement([2,2,1,3,1,1,2,2]))