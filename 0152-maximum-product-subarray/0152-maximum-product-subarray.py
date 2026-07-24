class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod=nums[0]
        minprod=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>=0: 
                maxprod=max(maxprod*nums[i],nums[i])
                minprod=min(minprod*nums[i],nums[i])
            else:
                temp=maxprod
                maxprod=max(minprod*nums[i],nums[i])
                minprod=min(temp*nums[i],nums[i])
            result=max(result,maxprod)
        return result