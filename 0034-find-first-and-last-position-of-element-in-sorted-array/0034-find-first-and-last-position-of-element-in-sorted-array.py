class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.findleft(nums,target)
        right=self.findright(nums,target)
        return [left,right]
    def findright(self,nums,target):
        n=len(nums)
        left=0
        right=n-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                ans=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
        return ans
    def findleft(self,nums,target):
        n=len(nums)
        left=0
        right=n-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                ans=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
        return ans