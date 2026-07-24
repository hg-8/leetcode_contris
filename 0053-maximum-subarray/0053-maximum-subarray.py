class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsofar=nums[0]
        currentsum=nums[0]
        for i in range(1,len(nums)):
            if currentsum<0:
                currentsum=0
            currentsum+=nums[i]
            if currentsum>maxsofar:
                maxsofar=currentsum
        return maxsofar
                