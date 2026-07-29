class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht={}
        n=len(nums)
        ans=[]
        for i in range(n):
            key=target-nums[i]
            if key in ht:
                ans=[ht[key],i]
                break
            ht[nums[i]]=i
        return ans