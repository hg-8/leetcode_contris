class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans=[]
        de=Deque()
        de.append(0)
        for i in range(1,k):
            while(len(de)>0 and nums[de[-1]]<nums[i]):
                de.pop()
            de.append(i)
        ans.append(nums[de[0]])
        for j in range(k,n):
            startpt=j-k+1
            while(len(de)>0 and de[0]<startpt):
                de.popleft()
            while(len(de)>0 and nums[de[-1]]<nums[j]):
                de.pop()
            de.append(j)
            ans.append(nums[de[0]])
        return ans
        
        