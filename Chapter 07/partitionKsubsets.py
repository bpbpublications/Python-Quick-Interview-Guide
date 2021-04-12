class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target = sum(nums)//k
        rem = sum(nums)%k
        sets = [[] for i in range(k)]
        if rem: return False
        #Define nested function
        def search(groups):
            print(nums,groups)
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                #print(i,group)
                if group + v <= target:
                    groups[i] += v
                    sets[i].append(v)
                    if search(groups):return True
                    groups[i] -= v
                    sets[i].pop(v)
                if not group: 
                    break
            nums.append(v)
            return False
        #Resume main
        nums.sort()
        if nums[-1] > target: return False
        if search([0] * k):
            print(sets)
            return True
        else:return False
#Driver code
sol=Solution()
#nums = [1, 1, 3, 2, 2]
#print(sol.canPartitionKSubsets(nums,3))
#nums = [4, 3, 2, 3, 5, 2, 1]
#print(sol.canPartitionKSubsets(nums,4))
nums = [1,9,1,1,8,2,5,3,1,3,6,3,3,4]
print(sol.canPartitionKSubsets(nums,5))