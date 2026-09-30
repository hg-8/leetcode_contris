class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n=len(nums)
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                return mid
        return start