from typing import List  #Not needed when submitting to Leet code
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            new_output = []
            for curr in output:
                new_output += [curr + [num] ]
            output += new_output
        return output
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n): # Loop over 2^N combinations
            bits = bin(i)[2:].zfill(n)
            output += [[nums[j] for j in range(n) if bits[j] == '1']]
        return output
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        for i in range(2**n): # Loop over 2^N combinations
            temp = i # Convert temp to binary
            temparr = []
            for j in range(n):
                if temp%2: temparr.append(nums[j])
                temp = temp//2
            output += [temparr]
        return output
"""
sol = Solution()
print(sol.subsets([1,2,3]))


