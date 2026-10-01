class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        start=1
        ans=1
        end=position[-1]-position[0]
        while start<=end:
            mid=(start+end)//2
            if (self.distanceposs(position,m,mid)):
                ans=mid
                start=mid+1
            else:
                end=mid-1
        return ans
    def distanceposs(self,position,m,dist):
        balls=1
        lastpos=position[0]
        for i in range(1,len(position)):
            if (position[i]>=lastpos+dist):
                balls+=1
                lastpos=position[i]
        if balls<m:
            return False
        else:
            return True
