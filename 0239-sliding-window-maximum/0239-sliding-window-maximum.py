class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        de=Deque()
        ans=[]
        for i,val in enumerate(nums):
            if de and de[0]<i-k+1:
                de.popleft()
            while de and nums[de[-1]]<val:
                de.pop()
            de.append(i)
            if i>=k-1:
                ans.append(nums[de[0]])
        return ans
        