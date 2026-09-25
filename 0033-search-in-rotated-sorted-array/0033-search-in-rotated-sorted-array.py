class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        start=0
        end=n-1
        while start<end:
            mid=(start+end)//2
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        por=start
        def bs(left,right):
            while left<=right:
                mid=(left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return -1
        if por==0:
            return bs(0,n-1)
        if nums[por]<=target<=nums[n-1]:
            return bs(por,n-1)
        else:
            return bs(0,por-1)

