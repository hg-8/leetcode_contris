class Solution:
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     ans=[]
    #     i=0
    #     nums.sort()
    #     n=len(nums)
    #     while i<n:
    #         if (i==0 or (i-1>=0 and nums[i-1]!=nums[i])):
    #             firstElement=nums[i]
    #             target=0-firstElement
    #             pairs=self.twosum(nums,i+1,n-1,target)
    #             for pair in pairs:
    #                 triplet=[firstElement,pair[0],pair[1]]
    #                 ans.append(triplet)
    #         i+=1
    #     return ans
    # def twosum(self,nums,start,end,target):
    #     pairs=[]
    #     small=start
    #     large=end
    #     while small<large:
    #         if (small-1>=start) and (nums[small-1] == nums[small]) :
    #             small+=1
    #             continue
    #         if (large+1<=end) and (nums[large+1] == nums[large]):
    #             large-=1
    #             continue
    #         if (nums[small]+nums[large]) < target:
    #             small+=1
    #         elif (nums[small]+nums[large]) > target:
    #             large-=1
    #         else:
    #             pair=[nums[small],nums[large]]
    #             pairs.append(pair)
    #             small+=1 
    #     return pairs
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if (large+1<=end) and (nums[large+1] == nums[large]):
                large-=1
                continue
            if (nums[small]+nums[large]) < target:
                small+=1
            elif (nums[small]+nums[large]) > target:
                large-=1
            else:
                pair=[nums[small],nums[large]]
                pairs.append(pair)
                small+=1 
        return pairs

