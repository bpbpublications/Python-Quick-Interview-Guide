from typing import List  
'''
#List approach
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniques = []
        for i in nums:
            if i not in uniques:
                uniques.append(i)
            else:
                uniques.remove(i)
        return uniques.pop()

from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        
        for i in counts:
            if counts[i] == 1:
                return i
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
#Driver code    
sol = Solution()
print(sol.singleNumber([2,5,1,2,5]))