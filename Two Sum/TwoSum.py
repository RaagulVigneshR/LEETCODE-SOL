class Solution(object):
    def twoSum(self, nums, target):
        s={}
        for i,v in enumerate(nums):
            r=target-nums[i]
            if r in s:
                return [s[r],i]
            s[v]=i
        
