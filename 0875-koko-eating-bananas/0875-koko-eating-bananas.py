class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        start=1
        end=max(piles)
        ans=end
        while(start<=end):
            mid=(start+end)//2
            if (self.counthours(piles,mid)>h):
                start=mid+1
            else:    
                ans=mid
                end=mid-1
        return ans
    def counthours(self,piles,speed):
        noofhours=0
        for pile in piles:
            noofhours+=math.ceil(pile/speed)
        return noofhours
