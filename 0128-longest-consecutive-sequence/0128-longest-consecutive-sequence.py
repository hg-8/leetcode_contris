class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        for i in nums:
            if (i-1) not in nums:
                c=i
                count=1
                while (c+1) in nums:
                    count+=1
                    c+=1
                if count>ans:
                    ans=count
        return ans